from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import os, sys

class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys )
        
    @staticmethod
    def read_file(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def detect_data_drift(self,base_df, current_df, threshold=0.05) -> bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1,d2)
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({column: {
                    'p_value':float(is_same_dist.pvalue),
                    'drift_status':is_found
                }})
            drif_report_file_path = self.data_validation_config.drift_report_file_path
            # Create directory
            dir_path = os.path.dirname(drif_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path=drif_report_file_path, content=report)


        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def validate_number_of_columns(self, dataframe:pd.DataFrame) -> bool:
        try:
            num_of_columns = len(self.schema_config)
            logging.info(f'Required number of columns: {num_of_columns}')
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")
            if len(dataframe.columns) == num_of_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path


            # Read the data from train and test
            train_df = DataValidation.read_file(train_file_path)
            test_df = DataValidation.read_file(test_file_path)

            # Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_df)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all columns. \n"
            status = self.validate_number_of_columns(dataframe=test_df)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all columns. \n"

            # Check data drift
            status = self.detect_data_drift(base_df=train_df,current_df=test_df)
            dir_path = os.path.




        except Exception as e:
            raise NetworkSecurityException(e, sys)