import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_BASE_URL = os.environ.get("API_BASE_URL")

settings = Settings()