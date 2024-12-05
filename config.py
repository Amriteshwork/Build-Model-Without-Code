import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key-12345"
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_data")
    CACHE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {"csv", "txt", "xlsx", "json"}
    
    # Model saving configurations
    MODEL_SAVE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_models")
    VIZ_SAVE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_visualizations")
    
    # Cache configurations
    CACHE_THRESHOLD = 128  # Maximum number of items to store in cache
    CACHE_TIMEOUT = 3600  # Cache timeout in seconds
