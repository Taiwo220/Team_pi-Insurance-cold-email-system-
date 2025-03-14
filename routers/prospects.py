from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.prospect import Prospect
from database.crud import create_prospect, get_prospect

router = APIRouter(prefix="/prospects", tags=["prospects"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Prospect)
async def add_prospect(prospect: Prospect, db: Session = Depends(get_db)):
    return create_prospect(db, prospect)

@router.get("/{prospect_id}", response_model=Prospect)
async def read_prospect(prospect_id: int, db: Session = Depends(get_db)):
    prospect = get_prospect(db, prospect_id)
    if not prospect:
        raise HTTPException(status_code=404, detail="Prospect not found")
    return prospect