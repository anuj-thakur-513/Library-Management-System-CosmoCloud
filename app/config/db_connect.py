from pymongo.mongo_client import MongoClient
import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("./.env"))

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.library
studentsCollection = db['students']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)