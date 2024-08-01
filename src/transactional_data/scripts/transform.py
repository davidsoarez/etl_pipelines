import pandas as pd
from src.logger import Logger
from pycpfcnpj import cnpj, cpf

async def fill_values_not_a_number(data: pd.DataFrame) -> pd.DataFrame:
    '''Fill empty values with None value'''
    return data.where(pd.notnull(data), None)

async def convert_value_notation(column: str, data: pd.DataFrame) -> pd.DataFrame:
    '''Convert comma to dot in the specified column'''
    if column in data.columns:
        data[column] = data[column].astype(str).str.replace(',', '.')
    return data

async def remove_rows_with_invalid_values(data: pd.DataFrame) -> pd.DataFrame:
    '''Removes null and invalid data'''
    data = data.dropna()
    data = data[data['cpf'].apply(cpf.validate)]
    data = data[data['loja_mais_frequente'].apply(cnpj.validate)]
    data = data[data['loja_da_ultima_compra'].apply(cnpj.validate)]
    return data

async def process_dataframe(logger: Logger, tracking_id: str, data: pd.DataFrame) -> pd.DataFrame:
    '''Processes the data so that it is suitable for persistence in the database'''
    logger.info(f'[{tracking_id}] Start processing dataframe')
    
    try:
        # Convert value notations
        data = await convert_value_notation(column='ticket_medio', data=data)
        data = await convert_value_notation(column='ticket_da_ultima_compra', data=data)
        
        # Fill NaNs and process the 'incompleto' column
        data = await fill_values_not_a_number(data=data)
        data.fillna({'incompleto': 0}, inplace=True)
        
        # Remove rows with invalid values
        data = await remove_rows_with_invalid_values(data=data)
        
        logger.info(f'[{tracking_id}] Dataframe processing finished successfully')
    except Exception as e:
        logger.error(f'[{tracking_id}] Error processing dataframe: {e}')
        raise
    
    return data
