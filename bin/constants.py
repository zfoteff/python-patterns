import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#   Remote Database constants
#MONGO_CONNECTION_STRING = f"mongodb+srv://{os.environ['MONGO_USER']}:{os.environ['MONGO_PASSWORD']}@cluster0.yjy1g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#DEFAULT_COLLECTION_NAME = "orphan_blocks"
#DEFAULT_DATABASE_NAME = "chain_data"

#   Local Database Constants
DEV_MONGO_HOST = os.environ['DEV_MONGO_HOST']
DEV_MONGO_PORT = os.environ['DEV_MONGO_PORT']
DEV_MONGO_URL = os.environ['DEV_MONGO_URL']