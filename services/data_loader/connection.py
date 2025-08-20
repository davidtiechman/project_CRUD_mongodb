from pymongo import MongoClient
import os

class Connection:
    def __init__(self):
        self.HOST = os.environ.get("MONGO_HOST", "mongodb-service")
        self.PORT = int(os.environ.get("MONGO_PORT", 27017))
        self.DATABASE = os.environ.get("MONGO_DB", "test")
        self.COLLECTION = os.environ.get("MONGO_COLLECTION", "users")

        self.client = MongoClient(
            host=self.HOST,
            port=self.PORT,
        )

        self.db = self.client[self.DATABASE]

        self.collection = self.db[self.COLLECTION]
    def get_collection(self):
        return self.collection
    def get_db(self):
        return self.db