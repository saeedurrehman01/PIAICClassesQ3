from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

import uvicorn

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str

# In-memory database
students_db: Dict[int, Student] = {}

# Function to generate unique student id
def generate_student_id() -> int:
    return max(students_db.keys(), default=0) + 1

@app.get("/students")
async def get_students():
    return list(students_db.values())

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    student = students_db.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students")
async def create_student(student: Student):
    student.id = generate_student_id()
    students_db[student.id] = student
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, new_student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    new_student.id = student_id
    students_db[student_id] = new_student
    return new_student

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}

def start():
    uvicorn.run("Assignment1.main:app",host="127.0.0.1", port=8080, reload=True)