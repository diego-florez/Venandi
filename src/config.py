from pymongo import MongoClient
import os
import dotenv
dotenv.load_dotenv()

#MongoDB
MGURL = os.getenv("MGURL")
myclient = MongoClient(f"{MGURL}")
db = myclient["test"]