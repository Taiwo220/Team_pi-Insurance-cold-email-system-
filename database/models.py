from sqlalchemy import Column, Integer, String
from .database import Base


class ProspectDB(Base):
    __tablename__ = "prospects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    industry = Column(String)
    engagement_level = Column(String)
    objections = Column(String)