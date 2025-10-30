from sqlalchemy.orm import Session
from . import models, schemas
from .excel_utils import atualizar_planilha

def criar_resultado(db: Session, resultado: schemas.ResultadoCreate):
    db_resultado = models.Resultado(**resultado.dict())
    db.add(db_resultado)
    db.commit()
    db.refresh(db_resultado)

    atualizar_planilha(db_resultado)  # preenche o Excel
    return db_resultado
