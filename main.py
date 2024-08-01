import asyncio
from uuid import uuid4
from src.logger import Logger
from src.transactional_data.schema import TransactionalDataSchema
from src.config import Config
from src.transactional_data.scripts.extract import open_csv_file_data
from src.transactional_data.scripts.load import load_file_into_db
from src.transactional_data.scripts.transform import process_dataframe, remove_rows_with_invalid_values
from pandas import DataFrame


async def extract_data(logger: Logger, tracking_id: str) -> DataFrame:
    data = await open_csv_file_data(tracking_id=tracking_id, logger=logger)
    return await process_dataframe(tracking_id=tracking_id, data=data, logger=logger)


async def load_data(logger: Logger, tracking_id: str, data: DataFrame) -> None:
    data_to_load = data.to_dict(orient='records')
    await load_file_into_db(logger=logger, tracking_id=tracking_id, data=data_to_load, schema=TransactionalDataSchema)


async def validate_data(data: DataFrame) -> DataFrame:
    return await remove_rows_with_invalid_values(data=data)


async def main(logger: Logger):
    try:
        tracking_id = uuid4()
        logger.info(f'Starting ETL job with tracking ID: {tracking_id}')
        
        # Data Extraction and Transformation
        data = await extract_data(logger, tracking_id)
        
        # Data Loading
        await load_data(logger, tracking_id, data)
        
        # Data Validation
        only_valid_data = await validate_data(data)
        logger.info(f'Saving processed file in path: {Config.PATH_READY}/dados_validos.xlsx')
        only_valid_data.to_excel(f'{Config.PATH_READY}/dados_validos.xlsx', index=False, sheet_name='Dados Válidos')
        
        logger.info("ETL job completed successfully")
        
    except Exception as error:
        logger.exception(f'Erro executing ETL job: {error}')
        raise


if __name__ == "__main__":
    logger = Logger().get_logger()
    asyncio.run(main(logger))