import os
from pathlib import Path  # Import Path to define BASE_DIR
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from the .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# OpenWeatherMap API Key
API_KEY = os.getenv('API_KEY')  # Fixed: Removed the extra comma

# MySQL Database Config
DB_CONFIG = {
    'host': '127.0.0.1',                         # MySQL host (localhost or 127.0.0.1)
    'user': os.getenv('DB_CONFIG_user'),          # Your MySQL username from .env
    'password': os.getenv('DB_CONFIG_password'),  # Your MySQL password from .env
    'database': os.getenv('DB_CONFIG_database')   # Your MySQL database name from .env
}
