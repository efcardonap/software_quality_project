"""
src/models/database.py
In-memory storage for the application.

DEUDA TÉCNICA INTENCIONAL:
  - [CRÍTICA] Sin autenticación ni autorización
  - [ALTA]    Contador de IDs global mutable (no thread-safe)
  - [MEDIA]   Variable global sin encapsulamiento
"""

# [DEUDA ALTA] Variables globales mutables — no son thread-safe
_estudiantes: dict = {}
_materias: dict = {}
_notas: list = []
_nota_id_counter: int = 0   # [DEUDA] contador global sin lock


def get_estudiantes() -> dict:
    return _estudiantes


def get_materias() -> dict:
    return _materias


def get_notas() -> list:
    return _notas


def next_nota_id() -> int:
    global _nota_id_counter        # [DEUDA] uso de global — code smell
    _nota_id_counter += 1
    return _nota_id_counter


def reset_db() -> None:
    """Limpia toda la base de datos. Solo para pruebas."""
    global _estudiantes, _materias, _notas, _nota_id_counter
    _estudiantes = {}
    _materias = {}
    _notas = []
    _nota_id_counter = 0
