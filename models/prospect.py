from pydantic import BaseModel

class Prospect(BaseModel):
    recipient: str
    industry: str
    engagement_level: str
    objections: str
    company_name: str