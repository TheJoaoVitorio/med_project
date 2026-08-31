from sqlalchemy import Column, Integer, String, DateTime
from core.database import Base
import datetime

class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True, index=True)
    patient = Column(String, nullable=False)
    doctor = Column(String, nullable=False)
    symptoms = Column(String, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)