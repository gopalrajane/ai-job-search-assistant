from pydantic_settings import BaseSettings
from typing import List, Optional
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://jobassistant:password@localhost:5432/job_assistant_db"
    DATABASE_ECHO: bool = False
    
    # Backend
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    
    # CORS & Security
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # AI Models & APIs
    OPENAI_API_KEY: Optional[str] = None
    CLAUDE_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    
    # Job Search APIs
    LINKEDIN_API_KEY: Optional[str] = None
    INDEED_API_KEY: Optional[str] = None
    GLASSDOOR_API_KEY: Optional[str] = None
    JOBBY_API_KEY: Optional[str] = None
    
    # Security
    ENCRYPTION_KEY: Optional[str] = None
    AUDIT_LOG_ENABLED: bool = True
    SCAM_DETECTION_ENABLED: bool = True
    PII_REDACTION_ENABLED: bool = True
    PROMPT_INJECTION_DETECTION_ENABLED: bool = True
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = 60
    
    # File Upload
    MAX_UPLOAD_SIZE_MB: int = 10
    ALLOWED_FILE_TYPES: List[str] = ["pdf", "docx", "doc"]
    UPLOAD_DIR: str = "./uploads"
    
    # Frontend
    FRONTEND_URL: str = "http://localhost:3000"
    
    # Google Cloud
    GCP_PROJECT_ID: Optional[str] = None
    GCP_REGION: str = "us-central1"
    GCP_BUCKET_NAME: Optional[str] = None
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Observability
    OTEL_ENABLED: bool = False
    OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://localhost:4317"
    GOOGLE_CLOUD_LOGGING_ENABLED: bool = False
    
    # Feature Flags
    FEATURE_MOCK_JOB_API: bool = True
    FEATURE_RESUME_ANALYSIS: bool = True
    FEATURE_COVER_LETTER_GENERATION: bool = True
    FEATURE_INTERVIEW_PREP: bool = True
    FEATURE_SALARY_INSIGHTS: bool = True
    FEATURE_CAREER_ROADMAP: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
