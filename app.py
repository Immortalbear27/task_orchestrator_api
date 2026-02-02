# Imports:
from fastapi import FastAPI

# Initialise the app:
app = FastAPI()

@app.get("/")
def root():
    return{"message": "This is the root page. Please go to other page for further details."}

@app.get("/health")
def health():
    return {"status": "all good"}

@app.post("/task")
async def task(task_type: str, payload: str, options = None):
    raise NotImplementedError

@app.post("/batch")
async def batch(tasklist):
    raise NotImplementedError

@app.get("/task/task_id")
async def task_task_id():
    raise NotImplementedError
