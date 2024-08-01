from pydantic import BaseModel, field_validator, Field, root_validator, validator
from datetime import datetime
from typing import Optional
import numpy as np

class TransactionalDataSchema(BaseModel):
    cpf: str
    private: Optional[bool]
    incompleto: Optional[bool]
    data_da_ultima_compra: Optional[datetime]
    ticket_medio: Optional[float]
    ticket_da_ultima_compra: Optional[float]
    loja_mais_frequente: Optional[str]
    loja_da_ultima_compra: Optional[str]
    
    @validator('data_da_ultima_compra')
    def parse_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, '%Y-%m-%d')
        return value
    
    @validator('incompleto')
    def parse_date(cls, value):
        if isinstance(value, type(np.nan)):
            return None
        return value