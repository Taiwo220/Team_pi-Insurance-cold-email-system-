from sqlalchemy.orm import Session
from .models import ProspectDB

def create_prospect(db: Session, prospect):
    db_prospect = ProspectDB(**prospect.dict())
    db.add(db_prospect)
    db.commit()
    db.refresh(db_prospect)
    return db_prospect

def get_prospect(db: Session, prospect_id: int):
    return db.query(ProspectDB).filter(ProspectDB.id == prospect_id).first()