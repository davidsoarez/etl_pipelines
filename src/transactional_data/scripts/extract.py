import os
import pandas as pd
from src.logger import Logger
from src.config import Config

async def open_csv_file_data(tracking_id: str, logger: Logger) -> pd.DataFrame:
    """
    Reads a CSV file into a pandas DataFrame.

    Args:
        tracking_id (str): Unique identifier for tracking the ETL job.
        logger (Logger): Logger instance for logging.
    """
    file_path = os.path.join(Config.PATH_RAW, 'Base.txt -Teste Técnico .txt')

    logger.info(f'[{tracking_id}] Opening CSV file at path: {file_path}')
    columns = [
        'cpf', 'private', 'incompleto', 'data_da_ultima_compra', 
        'ticket_medio', 'ticket_da_ultima_compra', 
        'loja_mais_frequente', 'loja_da_ultima_compra'
    ]

    try:
        df = pd.read_csv(file_path, sep='\s{2,}', names=columns, header=0, engine='python')
        logger.info(f'[{tracking_id}] Successfully read CSV file with {len(df)} rows.')
        return df
    except FileNotFoundError as e:
        logger.error(f'[{tracking_id}] File not found: {e}')
        raise
    except pd.errors.EmptyDataError as e:
        logger.error(f'[{tracking_id}] No data found in file: {e}')
        raise
    except pd.errors.ParserError as e:
        logger.error(f'[{tracking_id}] Error parsing CSV file: {e}')
        raise
    except Exception as e:
        logger.exception(f'[{tracking_id}] Unexpected error when reading CSV file: {e}')
        raise
