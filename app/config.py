import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "mysecretkey")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

SESSION_EXPIRE_SECONDS = int(os.getenv("SESSION_EXPIRE_SECONDS", 3600))