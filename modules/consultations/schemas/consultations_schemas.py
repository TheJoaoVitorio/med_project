from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ConsultationBase(BaseModel):
    patient: str
    doctor: str
    symptoms: str
    status: Optional[str] = "pending"

class ConsultationCreate(ConsultationBase):
    pass

class ConsultationResponse(ConsultationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) # permite ler os atributos do modelo SQLAlchemy e convertê-los em um dicionário para a resposta da API