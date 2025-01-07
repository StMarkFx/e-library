import bcrypt
import pymongo
from pymongo.errors import DuplicateKeyError, ConnectionFailure
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError
import reflex as rx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from difflib import SequenceMatcher

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class User(BaseModel):
    _id: Optional[str] = Field(None, alias="_id")  # MongoDB ID
    email: str = Field(...)
    password: str = Field(...)
    display_name: str = Field(...)
    avatar: Optional[str] = None
    faculty: str = Field(...)
    department: str = Field(...)
    level: str = Field(...)
    interests: List[str] = Field([])
    all_interactions: List[str] = Field([]) #Track all interactions for recommendations


class Resource(BaseModel):
    _id: Optional[str] = Field(None, alias="_id")  # MongoDB ID
    title: str = Field(...)
    author: str = Field(...)
    description: str = Field(...)
    faculty: str = Field(...)
    department: str = Field(...)
    level: str = Field(...)
    upload_date: str = Field(...)
    keywords: List[str] = Field([])
    uploader_id: str = Field(...) #Store uploader ID
    approval_status: str = Field("pending") #Default to pending


class State(rx.State):
    user: Optional[User] = None
    search_query: str = ""
    resources: List[Resource] = []
    recommendations: List[Resource] = [] #Store recommendations separately
    db: Optional[pymongo.database.Database] = None
    error_message: Optional[str] = None #For displaying errors


    def __init__(self):
        super().__init__()
        try:
            self.db = pymongo.MongoClient()["dlcf_elibrary"]
        except ConnectionFailure as e:
            self.error_message = f"Error connecting to MongoDB: {e}"


    def extract_keywords(self, text: str, num_keywords: int = 10) -> List[str]:
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        filtered_tokens = [lemmatizer.lemmatize(w) for w in tokens if w.isalnum() and w not in stop_words]
        return filtered_tokens[:num_keywords]


    def get_user_by_id(self, user_id: str) -> Optional[User]:
        try:
            user_data = self.db["users"].find_one({"_id": user_id})
            return User(**user_data) if user_data else None
        except Exception as e:
            self.error_message = f"Error fetching user: {e}"
            return None


    @rx.event(name="create_user")
    def create_user(self, email: str, password: str, display_name: str, faculty: str, department: str, level: str, interests: List[str]):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            new_user = User(email=email, password=hashed_password, display_name=display_name, faculty=faculty, department=department, level=level, interests=interests, all_interactions=[])
            result = self.db["users"].insert_one(new_user.model_dump(by_alias=True))
            self.user = self.get_user_by_id(str(result.inserted_id))
        except (ValidationError, DuplicateKeyError, Exception) as e:
            self.error_message = f"Error creating user: {e}"


    @rx.event(name="authenticate_user")
    def authenticate_user(self, email: str, password: str):
        try:
            user_data = self.db["users"].find_one({"email": email})
            if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data["password"].encode('utf-8')):
                self.user = User(**user_data)
            else:
                self.error_message = "Invalid email or password"
        except Exception as e:
            self.error_message = f"Error authenticating user: {e}"


    def get_resources(self, query: dict = None) -> List[Resource]:
        try:
            if query is None:
                query = {}
            if self.search_query:
                query["$or"] = [
                    {"title": {"$regex": self.search_query, "$options": "i"}},
                    {"author": {"$regex": self.search_query, "$options": "i"}},
                    {"faculty": {"$regex": self.search_query, "$options": "i"}},
                    {"department": {"$regex": self.search_query, "$options": "i"}},
                    {"level": {"$regex": self.search_query, "$options": "i"}},
                ]
            resources_data = self.db["resources"].find(query)
            self.resources = [Resource(**resource_data) for resource_data in resources_data]
            return self.resources
        except Exception as e:
            self.error_message = f"Error fetching resources: {e}"
            return []


    @rx.event(name="create_resource")
    def create_resource(self, title: str, author: str, description: str, faculty: str, department: str, level: str):
        try:
            keywords = self.extract_keywords(title + " " + description)
            new_resource = Resource(title=title, author=author, description=description, faculty=faculty, department=department, level=level, upload_date=datetime.now().isoformat(), keywords=keywords, uploader_id=self.user._id)
            result = self.db["resources"].insert_one(new_resource.model_dump(by_alias=True))
            self.resources.append(Resource(**new_resource.model_dump())) #Update resources list
        except (ValidationError, Exception) as e:
            self.error_message = f"Error creating resource: {e}"


    def update_resource(self, resource_id: str, updates: dict) -> bool:
        try:
            result = self.db["resources"].update_one({"_id": resource_id}, {"$set": updates})
            return result.modified_count > 0
        except Exception as e:
            self.error_message = f"Error updating resource: {e}"
            return False


    def delete_resource(self, resource_id: str) -> bool:
        try:
            result = self.db["resources"].delete_one({"_id": resource_id})
            return result.deleted_count > 0
        except Exception as e:
            self.error_message = f"Error deleting resource: {e}"
            return False


    def get_user_resources(self, user_id: str) -> List[Resource]:
        try:
            user_resources = self.db["user_resources"].find({"user_id": user_id})
            resource_ids = [ur["resource_id"] for ur in user_resources]
            return self.get_resources({"_id": {"$in": resource_ids}})
        except Exception as e:
            self.error_message = f"Error fetching user resources: {e}"
            return []


    @rx.event(name="add_resource_to_collection")
    def add_resource_to_collection(self, resource_id: str):
        try:
            self.db["user_resources"].insert_one({"user_id": self.user._id, "resource_id": resource_id})
            self.user.all_interactions.append(resource_id) #Update user interactions
            self.db["users"].update_one({"_id": self.user._id}, {"$set": {"all_interactions": self.user.all_interactions}}) #Update in DB
        except Exception as e:
            self.error_message = f"Error adding resource to collection: {e}"


    @rx.event(name="remove_resource_from_collection")
    def remove_resource_from_collection(self, resource_id: str):
        try:
            self.db["user_resources"].delete_one({"user_id": self.user._id, "resource_id": resource_id})
            self.user.all_interactions.remove(resource_id) #Update user interactions
            self.db["users"].update_one({"_id": self.user._id}, {"$set": {"all_interactions": self.user.all_interactions}}) #Update in DB
        except Exception as e:
            self.error_message = f"Error removing resource from collection: {e}"


    @rx.event(name="get_recommendations")
    def get_recommendations(self, num_recommendations: int = 5):
        try:
            if self.user:
                self.recommendations = self.content_based_filtering(self.user, num_recommendations)
            else:
                self.recommendations = self.get_resources(limit=num_recommendations) #Default recommendations if not logged in
        except Exception as e:
            self.error_message = f"Error getting recommendations: {e}"


    def content_based_filtering(self, user_profile: User, num_recommendations: int = 5) -> List[Resource]:
        interacted_resources = user_profile.all_interactions
        if not interacted_resources:
            return []

        keywords = set()
        for resource_id in interacted_resources:
            resource = self.get_resource_by_id(resource_id)
            if resource:
                keywords.update(resource.keywords)

        query = {"keywords": {"$in": list(keywords)}}
        resources = self.get_resources(query)
        resources.sort(key=lambda r: len(keywords.intersection(r.keywords)), reverse=True)
        return resources[:num_recommendations]


    def get_resource_by_id(self, resource_id: str) -> Optional[Resource]:
        try:
            resource_data = self.db["resources"].find_one({"_id": resource_id})
            return Resource(**resource_data) if resource_data else None
        except Exception as e:
            self.error_message = f"Error fetching resource: {e}"
            return None


    def get_user_profile(self, user_id: str) -> Optional[User]:
        return self.get_user_by_id(user_id)
