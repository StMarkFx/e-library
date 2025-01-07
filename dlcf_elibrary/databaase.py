import pymongo
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

MONGO_URI = os.getenv("MONGO_URI") # Get the MongoDB connection string from environment variables

client = pymongo.MongoClient(MONGO_URI)
