from src.exception import AppException
from src.logger.logs import logging
from src.components.data_ingestion import DataIngestion

obj = DataIngestion()
obj.initiate_data_ingestion()
print("Data Ingestion Completed!")