import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/llama-3.1-8b-instruct:free")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO") 