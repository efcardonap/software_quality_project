"""
main.py — Software Quality Project
FastAPI application entry point.

DEUDA TÉCNICA INTENCIONAL (para detección con SonarQube):
  - [MEDIA] Sin configuración de CORS
  - [MEDIA] Sin manejo global de excepciones
  - [BAJA]  Docstring de la app incompleto
"""
from fastapi import FastAPI
from src.routers import estudiantes, materias, notas

app = FastAPI(
    title="Software Quality Project",
    description="API de gestión académica",
    version="1.0.0"
)

app.include_router(estudiantes.router)
app.include_router(materias.router)
app.include_router(notas.router)


@app.get("/")
def root():
    return {"status": "ok", "message": "Software Quality API"}


@app.get("/health")
def health():
    return {"healthy": True}
