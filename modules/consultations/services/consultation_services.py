from sqlalchemy import text
from sqlalchemy.orm import Session
from modules.consultations.models.consultations_models import Consultation
from modules.consultations.schemas.consultations_schemas import ConsultationCreate, ConsultationResponse

async def create_consultation(db: Session, consultation: ConsultationCreate) -> ConsultationResponse:
    query = text("""
        INSERT INTO consultations (patient, doctor, symptoms, status, created_at, updated_at)
        VALUES (
            :patient,
            :doctor,
            :symptoms,
            :status,
            CURRENT_TIMESTAMP,
            CURRENT_TIMESTAMP
        )
        RETURNING id, patient, doctor, symptoms, status, created_at, updated_at;
    """)

    result = await db.execute(query, {
        "patient": consultation.patient,
        "doctor": consultation.doctor,
        "symptoms": consultation.symptoms,
        "status": consultation.status
    })

    row = result.fetchone()

    await db.commit()
    return ConsultationResponse(**dict(row._mapping))

        # VIA ORM 
    # db_consultation = Consultation(**consultation.model_dump())
    # db.add(db_consultation)
    # db.commit()
    # db.refresh(db_consultation)
    # return ConsultationResponse(**db_consultation.__dict__)

async def get_consultations(db: Session) -> list[ConsultationResponse]:
    query = text("SELECT id, patient, doctor, symptoms, status, created_at, updated_at FROM consultations;")
    result = await db.execute(query)
    
    return [dict(row._mapping) for row in result.fetchall()] # Convertendo a lista de resultados em dicionários

        # via ORM
    # consultations = db.query(Consultation).all() 
    # return [ConsultationResponse(**consultation.__dict__) for consultation in consultations]
