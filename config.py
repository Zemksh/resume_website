from dotenv import load_dotenv
import os

load_dotenv()

ALGORITHM = "HS256"
SECRET_KEY = os.getenv("SECRET_KEY")
ACESS_TOKEN_EXPIRE_MINUTES = 30

