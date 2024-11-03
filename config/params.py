import os
from dotenv import load_dotenv

load_dotenv("../.env")
params = {
    "API_KEY": os.getenv("API_KEY"),
}