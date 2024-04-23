import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.config.redis import limiter
from fastapi import Request


async def rate_limiter_middleware(request: Request, call_next):
    if request.url.path.__contains__("students"):
        user_id = request.headers.get("user-id")
        if not user_id:
            raise HTTPException(status_code=400, detail="User ID not provided")
        
        curr_date = datetime.date.today()
        redis_key = f"user_id:{user_id}:{curr_date}"
        
        redis_result = limiter(key=redis_key, limit=5)  # Adjust the limit as needed
        
        if not redis_result["call"]:
            return JSONResponse(content={"error": "API Call Limit Reached, Please try again tomorrow"}, status_code=503)
        
    response = await call_next(request)
    return response