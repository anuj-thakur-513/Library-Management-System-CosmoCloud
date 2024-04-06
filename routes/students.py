from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Optional
from models.student import Student
from config.dbConnect import studentsCollection

students = APIRouter()

@students.post("/students")
def create_student(student: Student):
    # convert student into student dump to insert into mongo
    student_dict = student.model_dump()
    inserted_student = studentsCollection.insert_one(student_dict)
    
    # Check if insertion was successful
    if inserted_student.acknowledged:
        inserted_student_id = inserted_student.inserted_id
        return JSONResponse(content={"id": str(inserted_student_id)}, status_code=201)
    else:
        raise HTTPException(status_code=500, detail="Failed to insert student into the database")
    
    
@students.get("/students")
def get_students(country: Optional[str] = Query(None), age: Optional[int] = Query(None)):
    query = {}
    if country:
        query["address.country"] = country 
    
    if age is not None:
        query["age"] = {"$gte": age}
        
    result = studentsCollection.find(query, {"_id": 0, "address": 0})
    students = list(result)
    
    return JSONResponse(content={"data": students}, status_code=200) 