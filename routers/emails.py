from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.prospect import Prospect  # Import the Prospect model
from services.llm_service import generate_email_content
from services.email_service import send_email

router = APIRouter(prefix="/emails", tags=["emails"])

class EmailRequest(BaseModel):
    prospects: List[Prospect]  # Use the Prospect model here

class EmailResponse(BaseModel):
    message: str
    content: List[str]
    recipients: List[str]

@router.post("/generate", response_model=EmailResponse)
async def generate_email(request: EmailRequest):
    try:
        # Generate email content for each prospect
        email_contents = generate_email_content(request.prospects)

        # Send emails asynchronously
        for prospect, content in zip(request.prospects, email_contents):
            await send_email(
                recipient=prospect.recipient,
                subject=f"Unlock Innovation in Your {prospect.industry} Company with {prospect.company_name}",
                body=content
            )

        # Include the recipients in the response
        return {
            "message": "Emails sent successfully",
            "content": email_contents,
            "recipients": [prospect.recipient for prospect in request.prospects]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))