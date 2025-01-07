from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class User(BaseModel):
    _id: Optional[str] = Field(None, alias="_id")  # MongoDB ID
    email: EmailStr = Field(...)
    password: str = Field(...)  # Store hashed password
    display_name: str = Field(...)
    avatar: Optional[str] = None  # Path to avatar image
    faculty: str = Field(...)
    department: str = Field(...)
    level: str = Field(...)
    interests: List[str] = Field([])
    all_interactions: List[str] = Field([])


class Resource(BaseModel):
    _id: Optional[str] = Field(None, alias="_id")  # MongoDB ID
    title: str = Field(...)
    author: str = Field(...)
    description: str = Field(...)
    faculty: str = Field(...)
    department: str = Field(...)
    level: str = Field(...)
    upload_date: datetime = Field(default_factory=datetime.utcnow)
    keywords: List[str] = Field([])
    uploader_id: str = Field(...)  # ID of the user who uploaded
    file_path: str = Field(...) #Path to the uploaded file
    approval_status: str = Field("pending")  # pending, approved, rejected


class ResourceUpload(BaseModel): #For handling uploads
    file: bytes = Field(...)
    title: str = Field(...)
    author: str = Field(...)
    description: str = Field(...)
    faculty: str = Field(...)
    department: str = Field(...)
    level: str = Field(...)
