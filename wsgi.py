from app import app
import os
from dotenv import load_dotenv

load_dotenv(".env")

if __name__ == "__main__":
    app.run()