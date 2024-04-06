from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.student import Student
from config.dbConnect import studentsCollection
from schemas.student import student_entity, students_entity


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