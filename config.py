import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
CHARACTER_PATH = os.getenv("CHARACTER_PATH")

CATEGORY_URL = f"{BASE_URL}{CHARACTER_PATH}"