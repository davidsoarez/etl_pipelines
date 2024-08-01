from asyncio import current_task

from contextlib import asynccontextmanager
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from src.database import Base

from src.config import Config
from src.logger import Logger


class PostgresDatabase:

    def __init__(self, db_url: str, logger: Logger) -> None:
        self._engine = create_async_engine(db_url, echo=False, pool_size=int(Config.SQL_POOL_SIZE),
                                           max_overflow=int(Config.SQL_MAX_OVERFLOW))
        self._session_factory = async_scoped_session(
            orm.sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession), scopefunc=current_task)
        self.logger = logger

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception:
            self.logger.exception('Postgres Session rollback because of exception')
            await session.rollback()
            raise
        finally:
            await session.close()
            await self._session_factory.remove()
