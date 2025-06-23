import os
from PIL import Image
from io import BytesIO
from pymongo import MongoClient
import gridfs

# MongoDB connection (update with your connection string if needed)
MONGO_URI = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/"
DB_NAME = "bizcardx"
COLLECTION_NAME = "image_data"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
fs = gridfs.GridFS(db)


def save_image_to_mongodb(image_file, user_id: str, image_name: str) -> str:
    """
    Saves uploaded image to MongoDB GridFS.
    Returns the MongoDB file_id.
    """
    image_data = image_file.read()
    file_id = fs.put(image_data, filename=image_name, user_id=user_id)
    return str(file_id)


def get_image_from_mongodb(image_name: str, user_id: str) -> Image.Image:
    """
    Retrieves an image from MongoDB GridFS by image_name and user_id.
    Returns a PIL Image object.
    """
    file_obj = fs.find_one({"filename": image_name, "user_id": user_id})
    if file_obj:
        image_stream = BytesIO(file_obj.read())
        return Image.open(image_stream)
    else:
        raise FileNotFoundError(f"No image found for {image_name} and user {user_id}")


def delete_image_from_mongodb(image_name: str, user_id: str):
    """
    Deletes an image from MongoDB GridFS by image_name and user_id.
    """
    file_obj = fs.find_one({"filename": image_name, "user_id": user_id})
    if file_obj:
        fs.delete(file_obj._id)


def resize_image(image: Image.Image, size=(470, 300)) -> Image.Image:
    """Resizes a PIL image."""
    return image.resize(size)
