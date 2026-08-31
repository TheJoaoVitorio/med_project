from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from modules.consultations.services import consultation_services 
from modules.consultations.schemas.consultations_schemas import ConsultationCreate, ConsultationResponse

router = APIRouter(prefix="/consultations", tags=["Consultations"])

@router.get("/", response_model=list[ConsultationResponse])
async def get_consultations(db: Session = Depends(get_db)):
    return await consultation_services.get_consultations(db)

@router.post("/create", response_model=ConsultationResponse)
async def create_consultation(consultation: ConsultationCreate, db: Session = Depends(get_db)):
    return await consultation_services.create_consultation(db, consultation)