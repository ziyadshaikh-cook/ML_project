from src.ML_project.components.data_ingestion import DataIngestion
from src.ML_project.components.data_transformation import DataTransformation
from src.ML_project.components.model_trainer import ModelTrainer
from src.ML_project.exception import CustomException
from src.ML_project.logger import logging
import sys

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            logging.info("Training pipline started")

            #step 1: Data Ingestion 
            logging.info("Starting data ingestion")
            train_data_path , test_data_path = self.data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion complete. Train:{train_data_path},Test:{test_data_path}")

            #step 2: Data Transformation   
            logging.info("Starting data transformation")
            train_arr , test_arr , preprocessor_path = self.data_transformation.initiate_data_transformation(
                train_data_path , test_data_path
            )
            logging.info("Data transformation complete") 

            #step 3 : Model Training
            logging.info("Starting Model training")
            r2_score = self.model_trainer.initiate_model_trainer(train_arr,test_arr)
            logging.info(f"Model training completed. Best model R2 score: {r2_score}")

            return r2_score

        except Exception as e:
            raise CustomException(e,sys)                 