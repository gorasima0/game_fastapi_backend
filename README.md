# 🎮 Game FastAPI Backend

A simple backend application built with **FastAPI** and **Python**.

This project demonstrates how to create a RESTful API for managing games and game studios. It is designed for learning backend development, working with databases, and understanding API operations.

## 🚀 Technologies Used

- 🐍 **Python** — Main programming language
- ⚡ **FastAPI** — Modern web framework for building APIs
- 🦄 **Uvicorn** — ASGI server for running the application
- 🗄️ **SQLAlchemy** — ORM for database interactions
- 📦 **Pydantic** — Data validation and serialization

## 📋 Prerequisites

Before running the project, make sure you have installed:

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional)

## ⚙️ Installation Guide

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/game_fastapi_backend.git
```

Navigate to the project directory:

```bash
cd game_fastapi_backend
```

### 2. Create a Virtual Environment

Create a virtual environment to keep project dependencies isolated:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn sqlalchemy
```

Alternatively, if the project contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

Once the server starts successfully, the application will be available at:

**http://127.0.0.1:8000**

The `--reload` option automatically restarts the server whenever changes are made to the source code.

## 📚 API Documentation

FastAPI provides automatically generated interactive API documentation.

**Swagger UI:**

http://127.0.0.1:8000/docs

**ReDoc:**

http://127.0.0.1:8000/redoc

Using Swagger UI, you can test API endpoints directly from your browser without installing additional software.

## 🎯 Project Purpose

The main goal of this project is to practice backend development using FastAPI.

The project focuses on:

- Creating RESTful API endpoints
- Working with HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Performing CRUD operations
- Creating and managing database models
- Implementing relationships between database tables
- Validating request and response data
- Handling API errors and HTTP status codes

## 🛠️ Development

This project is intended for educational purposes and can be extended with additional features such as:

- User authentication and authorization
- JWT tokens
- Advanced database queries
- API testing
- Docker support

## 📄 License

This project is created for educational and learning purposes.
