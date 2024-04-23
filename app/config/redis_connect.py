import redis
import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("./.env"))

try:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    print("Connected successfully to Redis")
except Exception as e:
    print(f"Error occured while connecting to Redis: {e}")
