from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.students import students

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(students)