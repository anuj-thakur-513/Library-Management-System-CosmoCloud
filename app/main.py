from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.students import students
from app.middlewares.rate_limiter import rate_limiter_middleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.middleware("http")(rate_limiter_middleware)

app.include_router(students)
