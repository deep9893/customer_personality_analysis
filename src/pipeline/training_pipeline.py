import os
import sys
from src.logger.logs import logging
from src.exception import AppException
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer
from dataclasses import dataclass


@dataclass
class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion = DataIngestion()
            self.data_validation = DataValidation()
            self.data_transformation = DataTransformation()
            self.model_trainer = ModelTrainer()
        except Exception as e:
            raise AppException(e, sys) from e

    def start_training_pipeline(self):
        try:
            logging.info(f"{'='*20}Training pipeline started.{'='*20} ")
            self.data_ingestion.initiate_data_ingestion()
            self.data_validation.initiate_data_validation()
            self.data_transformation.initiate_data_transformation()
            self.model_trainer.initiate_model_trainer()
        except Exception as e:
            raise AppException(e, sys) from e
