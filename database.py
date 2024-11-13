#NeitXD
# database.py
from pymongo import MongoClient
import os
import logging

logging.basicConfig(level=logging.INFO)
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = MongoClient(MONGO_DB_URL)
db = client['faceswap_db']
users_collection = db['users']

def add_user(user_id, credits=0):
    try:
        users_collection.update_one(
            {"user_id": user_id},
            {"$setOnInsert": {"credits": credits}},
            upsert=True
        )
    except Exception as e:
        logging.error(f"Error adding user: {e}")

def get_user(user_id):
    try:
        return users_collection.find_one({"user_id": user_id})
    except Exception as e:
        logging.error(f"Error retrieving user: {e}")
        return None

def update_credits(user_id, amount):
    try:
        users_collection.update_one(
            {"user_id": user_id},
            {"$inc": {"credits": amount}}
        )
    except Exception as e:
        logging.error(f"Error updating credits: {e}")

def extract_db():
    try:
        return list(users_collection.find())
    except Exception as e:
        logging.error(f"Error extracting database: {e}")
        return []
