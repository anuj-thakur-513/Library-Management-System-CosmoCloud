import redis
from datetime import datetime

client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def limiter(key, limit):
    # calculating TTL using time left in current day
    current_datetime = datetime.now()
    end_of_day = datetime(current_datetime.year, current_datetime.month, current_datetime.day, 23, 59, 59)
    time_remaining = end_of_day - current_datetime
    ttl_seconds = int(time_remaining.total_seconds())
    
    req = client.incr(key)
    if req == 1:
        client.expire(key, ttl_seconds)
        ttl = ttl_seconds
    else:
        ttl = client.ttl(key)
    if req > limit:
        return {
            "call": False,
            "ttl": ttl
        }
    else:
        return {
            "call": True,
            "ttl": ttl
        }
