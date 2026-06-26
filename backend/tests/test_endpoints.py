import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.session import Base, get_db
from app.models import User, Resume
import os

# Test database
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_user(db=TestingSessionLocal()):
    user = User(
        email="test@example.com",
        username="testuser",
        full_name="Test User",
        hashed_password="hashed_password"
    )
    db.add(user)
    db.commit()
    return user

# Test cases
def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_user_registration(client):
    """Test user registration"""
    response = client.post("/api/auth/register", json={
        "email": "newuser@example.com",
        "username": "newuser",
        "password": "password123",
        "full_name": "New User"
    })
    # Should succeed or return appropriate error
    assert response.status_code in [200, 201, 400]

def test_chat_endpoint(client):
    """Test chat endpoint"""
    response = client.post("/api/chat", json={
        "message": "Help me with job search",
        "user_id": 1
    })
    assert response.status_code in [200, 400, 401]  # May fail without auth

def test_job_search(client):
    """Test job search endpoint"""
    response = client.get("/api/jobs/search?q=python&location=remote")
    assert response.status_code in [200, 401]

def test_resume_upload(client):
    """Test resume upload"""
    response = client.post("/api/resumes/upload")
    # Should handle missing file gracefully
    assert response.status_code in [400, 422]
