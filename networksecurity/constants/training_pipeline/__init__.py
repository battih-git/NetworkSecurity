import os, sys
import numpy as np 
import pandas as pd


'''
Defining constant for training pipeline
'''
TARGET_COLUMN = 'Result'
PIPELIN_NAME:str =  'NetworkSecurity'
ARTIFACT_DIR:str = 'Artifacts'
FILE_NAME:str = 'NetwrorkData.csv'

TRAIN_FILE_NAME:str = 'train.csv'
TEST_FILE_NAME:str = 'test.csv' 

'''
Data Ingestion related constant start with DATAINGESTION VAR NAME
'''

DATA_INGESTION_COLLECTION_NAME: str = 'NetworkData'
DATA_INGESTION_DATABASE_NAME: str = 'HUZEFA'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_NAME: str = 'feature_store'
DATA_INGESTION_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2
