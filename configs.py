#NeitXD
# configs.py
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1001234567890"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))
LOW_CREDIT_THRESHOLD = int(os.getenv("LOW_CREDIT_THRESHOLD", "2"))
