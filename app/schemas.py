from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., example="admin")
    password: str = Field(..., example="admin123")


class LoginResponse(BaseModel):
    message: str
    access_token: str
    token_type: str


class UserProfileResponse(BaseModel):
    username: str
    role: str
    message: str