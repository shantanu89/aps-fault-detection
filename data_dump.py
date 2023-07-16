import pymongo
import pandas as pd
import json
from sensor.config import mongo_client


COPY_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__=="__main__":
    df=pd.read_csv(COPY_FILE_PATH)
    print(f"Rows and Columns:{df.shape}")

    #Converting dataframe into the json format so that we can dump data into the mongo db

    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
