
from datetime import datetime
import os, sys 
from networksecurity.constants import training_pipeline

print(training_pipeline.PIPELIN_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.pipeline_name = training_pipeline.PIPELIN_NAME
        self.arificat_name = training_pipeline.ARTIFACT_DIR
        self.arificat_dir = os.path.join(self.arificat_name,timestamp)
        self.timestamp:str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(
            training_pipeline_config.arificat_dir, training_pipeline.DATA_INGESTION_DIR
        )

        self.feature_store_file_path:str = os.path.join(
            training_pipeline_config.arificat_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_NAME
        )

        self.training_file_path:str = os.path.join(
            training_pipeline_config.arificat_dir, training_pipeline.DATA_INGESTION_DIR, training_pipeline.TRAIN_FILE_NAME
        )

        self.testing_file_path:str = os.path.join(
            training_pipeline_config.arificat_dir, training_pipeline.DATA_INGESTION_DIR, training_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio:str = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str =training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str = training_pipeline.DATA_INGESTION_DATABASE_NAME


class DataValidationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.arificat_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str = os.path.join(
            self.valid_data_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT, training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )