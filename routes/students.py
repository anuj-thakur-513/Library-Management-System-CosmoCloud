from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Optional
from bson import ObjectId
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


@students.get("/students/{id}")
def get_student(id: str):
    student = studentsCollection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    # check if the student was found or not
    if student: 
        return JSONResponse(content=student, status_code=200)
    else:
        return HTTPException(status_code=404, detail="Student not Found!")