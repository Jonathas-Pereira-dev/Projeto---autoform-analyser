from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Formulario(Base):
    __tablename__ = "formularios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    criado_em = Column(DateTime, default=datetime.utcnow)

    resultados = relationship("Resultado", back_populates="formulario")

class Resultado(Base):
    __tablename__ = "resultados"
    id = Column(Integer, primary_key=True, index=True)
    formulario_id = Column(Integer, ForeignKey("formularios.id"))
    operador = Column(String, nullable=False)
    observacoes = Column(String)
    dados = Column(JSON)  # guarda respostas do formulário
    criado_em = Column(DateTime, default=datetime.utcnow)

    formulario = relationship("Formulario", back_populates="resultados")
