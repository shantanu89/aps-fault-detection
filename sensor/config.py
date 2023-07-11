import pymongo
import pandas as pd
import json,os
from dataclasses import dataclass
TARGET_COLUMN = "class"

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


env_var=EnvironmentVariable()

mongo_client=pymongo.MongoClient(env_var.mongo_db_url)
