from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoForm Analyser")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/resultado", response_model=schemas.ResultadoOut)
def criar_resultado(resultado: schemas.ResultadoCreate, db: Session = Depends(get_db)):
    return crud.criar_resultado(db, resultado)
