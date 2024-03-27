from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse  
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


def sum(num1,num2):   # backend  process result 
    return num1 + num2

def subtract(num1,num2): # backend process result
    return num1 - num2

@app.get('/')
def home():
    return {'data': 20}

@app.post('/add')  # POST method APi 
def add(numberA: int =Query(...), numberB: int =Query(...) ):
    return {"sum": sum(numberA,numberB)}

@app.post('/subtract') # POST method APi
def sub(numberA: int =Query(...), numberB: int =Query(...) ):
    return {"subtract": subtract(numberA,numberB)}


uvicorn.run(app, host='0.0.0.0', port=80)