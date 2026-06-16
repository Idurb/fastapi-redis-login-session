from datetime import datetime, timedelta
from jose import jwt
from fastapi import HTTPException, status
from app.config import JWT_SECRET_KEY, JWT_ALGORITHM, SESSION_EXPIRE_SECONDS
from app.redis_client import redis_client


fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "idurbasha": {
        "username": "idurbasha",
        "password": "password123",
        "role": "user"
    }
}


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)

    if not user:
        return None

    if user["password"] != password:
        return None

    return user


def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(seconds=SESSION_EXPIRE_SECONDS)

    payload = data.copy()
    payload.update({"exp": expire})

    token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )

    return token


def login_user(username: str, password: str):
    user = authenticate_user(username, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token(
        data={
            "sub": user["username"],
            "role": user["role"]
        }
    )

    redis_key = f"session:{user['username']}"

    redis_client.setex(
        redis_key,
        SESSION_EXPIRE_SECONDS,
        token
    )

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }


def logout_user(username: str):
    redis_key = f"session:{username}"

    redis_client.delete(redis_key)

    return {
        "message": "Logout successful"
    }


def check_user_session(username: str, token: str):
    redis_key = f"session:{username}"

    stored_token = redis_client.get(redis_key)

    if not stored_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired or user logged out"
        )

    if stored_token != token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session token"
        )

    return True