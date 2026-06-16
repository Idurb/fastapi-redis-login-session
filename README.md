# FastAPI Redis Login Session

A production-ready authentication API built with **FastAPI**, **Redis**, and **JWT** that demonstrates login session management using Redis.

## 🚀 Features

* User Login
* JWT Authentication
* Redis Session Management
* Protected APIs
* Logout
* Session Expiration
* Environment Configuration using `.env`
* Docker Support
* Interactive Swagger API Documentation

---

# Tech Stack

* Python 3.11+
* FastAPI
* Redis
* Docker
* JWT Authentication
* Pydantic
* Uvicorn

---

# Project Structure

```text
fastapi-redis-login-session/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── redis_client.py
│   ├── auth_service.py
│   ├── dependencies.py
│   └── schemas.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Authentication Flow

```
Client
   │
   ▼
POST /login
   │
   ▼
Validate Credentials
   │
   ▼
Generate JWT Token
   │
   ▼
Store Session in Redis
   │
   ▼
Return JWT Token
```

### Access Protected APIs

```
Client
   │
Bearer Token
   │
   ▼
Protected API
   │
   ▼
JWT Validation
   │
   ▼
Redis Session Validation
   │
   ▼
Response
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/fastapi-redis-login-session.git

cd fastapi-redis-login-session
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Start Redis

Using Docker

```bash
docker run --name redis-server -p 6379:6379 -d redis
```

Check Container

```bash
docker ps
```

---

# Environment Variables

Create a `.env` file

```env
REDIS_HOST=localhost
REDIS_PORT=6379

JWT_SECRET_KEY=mysecretkey

JWT_ALGORITHM=HS256

SESSION_EXPIRE_SECONDS=3600
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## Login

**POST**

```
/login
```

Request

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response

```json
{
  "message": "Login successful",
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

---

## Get Profile

**GET**

```
/profile
```

Authorization Header

```
Bearer <JWT_TOKEN>
```

Response

```json
{
  "username": "admin",
  "role": "admin",
  "message": "You are accessing a protected route"
}
```

---

## Logout

**POST**

```
/logout
```

Authorization Header

```
Bearer <JWT_TOKEN>
```

Response

```json
{
  "message": "Logout successful"
}
```

---

# Redis Session Flow

```
Login

↓

JWT Generated

↓

Redis

session:admin

↓

JWT Token

↓

TTL = 3600 seconds

↓

Protected APIs

↓

Logout

↓

Redis Session Deleted
```

---

# Future Improvements

* User Registration
* Password Hashing (bcrypt)
* Refresh Tokens
* Role-Based Access Control (RBAC)
* Email Verification
* OTP Authentication
* Rate Limiting using Redis
* Docker Compose
* PostgreSQL Integration
* Unit Testing
* CI/CD Pipeline
* Kubernetes Deployment

---

# Learning Objectives

This project demonstrates:

* FastAPI Authentication
* JWT Token Generation
* Redis Session Storage
* Session Expiration
* Protected Routes
* Dependency Injection
* Environment Variable Management
* REST API Development

---

# License

This project is intended for learning and portfolio purposes.

---

# Author

**Idurbasha Shaik**

Backend Developer | Python | FastAPI | PostgreSQL | Redis | Docker

If you found this project helpful, consider giving it a ⭐ on GitHub.
