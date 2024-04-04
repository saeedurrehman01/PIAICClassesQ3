from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [{
    "Student ID": 301,
    "Name": "One",
    "Age": 15,
    "Grade": "6th"
},
{
    "Student ID": 302,
    "Name": "Two",
    "Age": 16,
    "Grade": "7th"
}]

# GET /students: Retrieve all students.
@app.get("/students")
def getStudents():
    return students

#  GET /students/{student_id}: Retrieve specific student details.
@app.get("/students/{studentID}")
def get_student(studentID: int):
    for student in students:
        if student["Student ID"] == studentID:
            return student

# POST /Students: Add a new student.
@app.post("/addStudent")
def addStudent(studentID:int,
                name:str,
                age:int,
                grade:str):
    global students
    students.append({"Student ID": studentID,
                     "Name": name,
                     "Age": age,
                     "Grade": grade
                     })
    return students

# PUT /students/{student_id}: Update a student's details.
@app.put("/students/{studentID}")
def update_student(studentID: int,
                    name: str,
                    age: int,
                    grade: str):
    for student in students:
        if student["Student ID"] == studentID:
            student["Name"] = name
            student["Age"] = age
            student["Grade"] = grade
            return student

# DELETE /students/{student_id}: Delete a student.
@app.delete("/students/{studentID}")
def deleteStudent(studentID: int):
    global students
    for student in students:
        if student["Student ID"] == studentID:
            students.remove(student)
            return {"message": "Student deleted successfully"}

def start():
   uvicorn.run ("todoss.main:app", host="127.0.0.1", port=8080, reload=True)