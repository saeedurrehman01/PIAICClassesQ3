from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/gettodos")
def getTodos():
    print("Get todos Called")
    return "gettodos called"

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get todo Called")
    return "getSingleTodo Called"


@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos Called")
    return "gettodos post method called"

def start():
    uvicorn.run("todolist.main:app",host="127.0.0.1", port=8080, reload=True)