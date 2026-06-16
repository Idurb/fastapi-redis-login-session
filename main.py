from fastapi import FastAPI, Depends
from app.schemas import LoginRequest, LoginResponse, UserProfileResponse
from app.auth_service import login_user, logout_user
from app.dependencies import get_current_user

app = FastAPI(
    title="FastAPI Redis Login Session API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI Redis Login Session API is running"
    }


@app.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    return login_user(
        request.username,
        request.password
    )


@app.get("/profile", response_model=UserProfileResponse)
def profile(current_user: dict = Depends(get_current_user)):
    return {
        "username": current_user["username"],
        "role": current_user["role"],
        "message": "You are accessing a protected route"
    }


@app.post("/logout")
def logout(current_user: dict = Depends(get_current_user)):
    return logout_user(current_user["username"])