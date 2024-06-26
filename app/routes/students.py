from fastapi import APIRouter, HTTPException, Query, Header
from fastapi.responses import JSONResponse
from typing import Optional
from bson import ObjectId
from app.models.student import Student
from app.config.db_connect import studentsCollection

students = APIRouter()

@students.post("/students")
def create_student(
    student: Student,
    user_id: str = Header(..., description="User ID calling the API")
):
    # capitalize required data before insertion
    student.address.city = student.address.city.capitalize()
    student.address.country = student.address.country.capitalize()
    # convert student into student dump to insert into mongo
    student_dict = student.model_dump()
    inserted_student = studentsCollection.insert_one(student_dict)
    
    # Check if insertion was successful
    if inserted_student.acknowledged:
        inserted_student_id = inserted_student.inserted_id
        return JSONResponse(content={"id": str(inserted_student_id)}, status_code=201)
    else:
        return HTTPException(status_code=500, detail="Failed to insert student into the database")
    
    
@students.get("/students")
def get_all_students(
    country: Optional[str] = Query(None),
    age: Optional[int] = Query(None), 
    user_id: str = Header(..., description="User ID calling the API")
):
    # construct find query as per country and age
    query = {}
    if country:
        query["address.country"] = country.capitalize() 
    
    if age is not None:
        query["age"] = {"$gte": age}
        
    result = studentsCollection.find(query, {"_id": 0, "address": 0})
    students = list(result)
    
    return JSONResponse(content={"data": students}, status_code=200) 


@students.get("/students/{id}")
def get_student(
    id: str,
    user_id: str = Header(..., description="User ID calling the API")
):
    student = studentsCollection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    # check if the student was found or not
    if student: 
        return JSONResponse(content=student, status_code=200)
    else:
        return HTTPException(status_code=404, detail="Student not Found!")
    

@students.patch("/students/{id}")
def update_student(
    id: str,
    name: Optional[str] = Query(None),
    age: Optional[int] = Query(None),
    city: Optional[str] = Query(None),
    country: Optional[str] = Query(None),
    user_id: str = Header(..., description="User ID calling the API")
):
    if name is None and age is None and city is None and country is None:
        return HTTPException(status_code=400, detail="At least one of the field needs to be updated")
    
    # construct query for user updation
    update_data = {}
    if name is not None:
        update_data["name"] = name
        
    if age is not None:
        update_data["age"] = age
        
    if city is not None or country is not None:
        update_data["address"] = {}
        if city is not None:
            update_data["address"]["city"] = city
        if country is not None:
            update_data["address"]["country"] = country
            
    result = studentsCollection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.modified_count == 0:
        return HTTPException(status_code=404, detail="Student not found!")
    
    return JSONResponse(content=None, status_code=204)


@students.delete("/students/{id}")
def delete_student(
    id: str,
    user_id: str = Header(..., description="User ID calling the API")
):
    result = studentsCollection.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count == 0:
        return HTTPException(status_code=404, detail="Student not found!")
    
    return JSONResponse(content={}, status_code=200)