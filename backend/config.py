import os

# Database
DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.db')

# API Keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'your-groq-api-key-here')

# App Settings
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Flask Config
FLASK_CONFIG = {
    'DEBUG': DEBUG,
    'SECRET_KEY': SECRET_KEY
}
