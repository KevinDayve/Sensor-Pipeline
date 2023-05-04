import os
import pymongo
import certifi
from dotenv import load_dotenv
load_dotenv()

ca = certifi.where()

class MongoDBOps:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(os.getenv("MONGODB_URI", None))
        self.db_name = os.getenv("DATABASE")
    def insert_many(self, collection_name: str, records: list):
        self.client[self.db_name][collection_name].insert_many(records)
    def insert(self, collection_name: str, records: list):
        self.client[self.db_name][collection_name].insert_one(records)


