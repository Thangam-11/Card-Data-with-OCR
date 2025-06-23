from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

class MongoDBHandler:
    def __init__(self, uri: str = None, db_name: str = "bizcardx", collection_name: str = "cards"):
        self.uri = uri or os.getenv("MONGO_DB_URI")
        if not self.uri:
            raise ValueError("MongoDB URI not found in environment variables.")

        self.client = MongoClient(self.uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data: dict):
        """Insert a new business card entry."""
        result = self.collection.insert_one(data)
        return result.inserted_id

    def get_all_data(self):
        """Retrieve all entries without Mongo _id."""
        return list(self.collection.find({}, {"_id": 0}))

    def update_data(self, query: dict, update_values: dict):
        """Update matching document with new values."""
        return self.collection.update_one(query, {"$set": update_values})

    def delete_data(self, query: dict):
        """Delete a document that matches the query."""
        return self.collection.delete_one(query)
