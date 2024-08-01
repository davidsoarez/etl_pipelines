from sqlalchemy import Column, Integer, String, Boolean, Date, Float
from src.database.base import Base

class TransactionalData(Base):
    __tablename__ = "transactional_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cpf = Column(String(25), nullable=True)
    private = Column(Integer, nullable=True, default=True)
    incompleto = Column(Integer, nullable=True, default=True)
    data_da_ultima_compra = Column(Date, nullable=True)
    ticket_medio = Column(Float, nullable=True)
    ticket_da_ultima_compra = Column(Float, nullable=True)
    loja_mais_frequente = Column(String(100), nullable=True)
    loja_da_ultima_compra = Column(String(100), nullable=True)
