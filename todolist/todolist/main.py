from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/gettodos/{id}")
def gettodos(id):
    print ("get todos called")
    return ("message: Test Todo List")

@app.post("/get_todos")
def get_todos():
    print ("get Post todos called")
    return ("message: Test Post Todo List")

get_todos()

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get todo Called")
    return "getSingleTodo called"

uvicorn.run("todolist.main:app", host="local", port=8080, reload=True )

