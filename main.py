from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime, date
from typing import Optional
from fastapi.staticfiles import StaticFiles

# Configuração do banco de dados
DATABASE_URL = "mysql+pymysql://admin:admin@172.28.208.1/subconjunto"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição do modelo de dados
class Subconjunto(Base):
    __tablename__ = "subconjuntos"
    id = Column(Integer, primary_key=True, index=True)
    dataehora = Column(DateTime, default=datetime.utcnow)
    nome = Column(String(60), nullable=False)
    linha = Column(Integer, nullable=False)
    idsub = Column(Integer, nullable=False)
    movimento = Column(String(60), nullable=False)
    data = Column(Date, nullable=True)
    defeito = Column(Text, nullable=False)
    tecnico = Column(Text, nullable=False)
    comentario = Column(Text, nullable=True)

Base.metadata.create_all(bind=engine)

# Definição do modelo de dados para a requisição
class SubconjuntoCreate(BaseModel):
    nome: str
    linha: int
    idsub: int
    movimento: str
    data: Optional[date]
    defeito: str
    tecnico: str
    comentario: Optional[str]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/subconjuntos/")
async def create_subconjunto(subconjunto: SubconjuntoCreate, db: Session = Depends(get_db)):
    db_subconjunto = Subconjunto(
        nome=subconjunto.nome,
        linha=subconjunto.linha,
        idsub=subconjunto.idsub,
        movimento=subconjunto.movimento,
        data=subconjunto.data,
        defeito=subconjunto.defeito,
        tecnico=subconjunto.tecnico,
        comentario=subconjunto.comentario
    )
    db.add(db_subconjunto)
    db.commit()
    db.refresh(db_subconjunto)
    return db_subconjunto

@app.get("/subconjuntos/")
async def read_subconjuntos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Subconjunto).offset(skip).limit(limit).all()
