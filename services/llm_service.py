import getpass
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import List, Dict
from models.prospect import Prospect 

# Load environment variables from .env file
load_dotenv()

# Ensure GROQ_API_KEY is set
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

def generate_email_content(prospects: List[Prospect]) -> List[str]:
    emails = []
    for prospect in prospects:
        company_name = prospect.company_name  # Access attributes directly
        recipient = prospect.recipient
        industry = prospect.industry
        engagement_level = prospect.engagement_level
        objections = prospect.objections

        prompt = f"""
        Write a cold email for a company in the {industry} industry. The recipient's name is {recipient}, and their engagement level is {engagement_level}. 
        Address the following objections: {objections}.

        The email should:
        1. Start with the recipient's name.
        2. Mention the industry and company name which is {company_name}.
        3. Highlight the engagement level.
        4. Address the objections directly.
        5. Be professional and concise.
        6. Focus on Industry-based Personalization for example If the prospect is in tech, emphasize innovation.If the prospect is in finance, emphasize security & ROI.If the prospect is in healthcare, emphasize compliance & efficiency, etc. Don't make it look like an AI generated it like having something like saying here is a cold email template that you can use. Instead, make it look like a human wrote it.
        7. For 'Best regards or salutation at the end , use 'Team Pi' 
        8. Do not include any introductory text like "Here is a cold email...".
        9.Do not use placeholders like [specific area of innovation] or [specific percentage]. Use actual data or general terms instead.
        """

        llm = ChatGroq(
            model="llama3-8b-8192",
            temperature=0.2,
            max_tokens=1000, 
            timeout=None,
            max_retries=2
        )

        response = llm.invoke(prompt)
        emails.append(response.content.strip())
    return emails