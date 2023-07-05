from src.exception import AppException
from src.logger.logs import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer
from src.pipeline.training_pipeline import TrainingPipeline



obj = DataIngestion()
obj.initiate_data_ingestion()
print("Data Ingestion Completed!")

obj = DataValidation()
obj.initiate_data_validation()
print("Data Validation Completed!")


obj = DataTransformation()
obj.initiate_data_transformation()
print("Data Transformation Completed!")

obj = ModelTrainer()
obj.initiate_model_trainer()
print("model_trainer Completed!")


obj = TrainingPipeline()
obj.start_training_pipeline()
print("training pipeline Completed!")