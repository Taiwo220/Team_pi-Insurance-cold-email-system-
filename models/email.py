from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/emails", tags=["emails"])

class EmailRequest(BaseModel):
    recipient: str  # Recipient's email address
    industry: str
    engagement_level: str
    objections: str
    company_name: str  # Add company name

class EmailResponse(BaseModel):
    message: str
    content: str
    recipient: str  # Add the recipient's email address