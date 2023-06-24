from src.exception import AppException
from src.logger.logs import logging
# from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation


# obj = DataIngestion()
# obj.initiate_data_ingestion()
# print("Data Ingestion Completed!")

obj = DataValidation()
obj.initiate_data_validation()
print("Data Validation Completed!")