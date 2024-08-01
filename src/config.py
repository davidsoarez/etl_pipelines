
class Config:
    SQL_POOL_SIZE: int = 5
    SQL_MAX_OVERFLOW: int = 10
    DB_ASYNC_CONN_URL: str = 'postgresql+asyncpg://postgres:secret@postgres:5432/service-database'
    LOG_LEVEL: str = 'DEBUG'
    BATCH_SIZE: int = 1000
    PATH_RAW:str = '/app/src/data/row'
    PATH_READY: str = '/app/src/data/ready'

    