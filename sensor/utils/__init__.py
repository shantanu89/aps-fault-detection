import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exeption import SensorException
import sys

def get_collection_as_dataframe(databasename:str,collectionname:str)->pd.DataFrame:
    try:
        df=pd.DataFrame(list(mongo_client[databasename,collectionname].find()))
    except Exception as e:
        raise SensorException(e, sys)