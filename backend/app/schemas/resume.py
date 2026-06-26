from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ResumeBase(BaseModel):
    filename: str

class ResumeCreate(ResumeBase):
    pass

class ResumeExtracted(BaseModel):
    skills: List[str]
    experience: List[dict]
    education: List[dict]
    projects: List[dict]
    summary: Optional[str]

class Resume(ResumeBase):
    id: int
    user_id: int
    file_path: str
    file_size: int
    skills: List[str]
    experience: List[dict]
    education: List[dict]
    projects: List[dict]
    summary: Optional[str]
    is_primary: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
