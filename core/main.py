from fastapi import FastAPI
from core.database import Base, engine
from modules.consultations.routes import consultations_routes

Base.metadata.create_all(bind=engine) # gera as tabelas no banco de dados
app = FastAPI(title="Medical Consultation API")

# Registra as rotas
app.include_router(consultations_routes.router)