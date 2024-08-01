from typing import List
from pydantic import ValidationError
from src.config import Config
from src.database.sessions import PostgresDatabase
from src.logger import Logger
from src.transactional_data.model import TransactionalData
from src.transactional_data.schema import TransactionalDataSchema


async def load_file_into_db(logger: Logger, tracking_id: str, data: List[dict], schema: TransactionalDataSchema) -> None:
    """
    Persists data into the database in batches.

    Args:
        logger (Logger): Logger instance for logging.
        tracking_id (str): Unique identifier for the ETL job.
        data (List[dict]): List of data dictionaries to be persisted.
        schema (TransactionalDataSchema): Schema class used for data validation.
    """
    db = PostgresDatabase(Config.DB_ASYNC_CONN_URL, logger)
    logger.info(f'[{tracking_id}] Start loading data into the database.')

    async with db.session() as session:
        transactions = []

        for item in data:
            try:
                # Validate and transform data
                validated_data = schema(**item)
                transaction_data = TransactionalData(
                    cpf=validated_data.cpf,
                    private=validated_data.private,
                    incompleto=validated_data.incompleto,
                    data_da_ultima_compra=validated_data.data_da_ultima_compra,
                    ticket_medio=validated_data.ticket_medio,
                    ticket_da_ultima_compra=validated_data.ticket_da_ultima_compra,
                    loja_mais_frequente=validated_data.loja_mais_frequente,
                    loja_da_ultima_compra=validated_data.loja_da_ultima_compra
                )
                transactions.append(transaction_data)

                # Commit in batches
                if len(transactions) >= Config.BATCH_SIZE:
                    logger.debug(f'[{tracking_id}] Committing {len(transactions)} records to the database.')
                    session.add_all(transactions)
                    await session.commit()
                    transactions.clear()

            except ValidationError as error:
                logger.error(f'[{tracking_id}] Validation error: {error}')
                # You might choose to continue processing other items despite validation errors

        # Commit any remaining transactions
        if transactions:
            logger.debug(f'[{tracking_id}] Committing remaining {len(transactions)} records to the database.')
            session.add_all(transactions)
            await session.commit()

    logger.info(f'[{tracking_id}] Data loading completed.')
