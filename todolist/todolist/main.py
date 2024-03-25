from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [{
    "userName":"Ali",
    "rollNo": 2342
},
            {
    "userName":"Naveed Sarwar",
    "rollNo": 9213
}
            ]

@app.get("/students")
def getStudents():
    return students

@app.get("/addStudent")
def addStudent(userName:str, rollNo:str):
    global students
    students.append({"userName":userName, "rollNo":rollNo})
    return students

@app.get("/")
def helloWorld():
    return {"hello": "world"}

@app.get("/gettodolist/{userName}/{rollNo}")
def gettodolist(userName:str, rollNo:str):
    print("Get todolist called",userName,rollNo)
    return userName + rollNo 

@app.post("/gettodolist")
def gettodolistPost():
    print("Get post method todolist called")
    return "post gettodolist called"

@app.get("/getSingleTodo")
def getSingleTodo(userName:str, rollNo:str):
    print("Get todo called",userName,rollNo )
    return "getSingleTodo called sadf sd sdff"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"
    

def start():
    uvicorn.run("todolist.main:app",host="127.0.0.1", port=8080, reload=True)