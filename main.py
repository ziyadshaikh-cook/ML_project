from src.ML_project.pipelines.training_pipelines import TrainPipeline
from src.ML_project.exception import CustomException
from src.ML_project.logger import logging
import sys

if __name__ == "__main__":
    try:
        pipeline = TrainPipeline()
        r2_score = pipeline.run_pipeline()
        print(f"\nTraining complete. Best model R2 Score:{r2_score}")
    except Exception as e:
        raise CustomException(e,sys)

