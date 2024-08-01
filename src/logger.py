import logging
from logging import Formatter, StreamHandler
from src.config import Config

class Logger:
    def __init__(self) -> None:
        # Configurar o logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(Config.LOG_LEVEL)
        
        # Criar e configurar o formatter
        formatter = Formatter(fmt='%(asctime)s [%(process)d] [%(funcName)s] [%(levelname)s] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
        
        # Criar e configurar o handler
        handler = StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(Config.LOG_LEVEL)
        
        # Adicionar o handler ao logger
        self.logger.addHandler(handler)
    
    def get_logger(self):
        return self.logger