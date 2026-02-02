# Imports:
from pydantic import BaseModel
from fastapi import FastAPI

# Initialise the app:
app = FastAPI()

# Specifies the type of input for each task:
class TaskFormat(BaseModel):
    task_type: str
    payload: str
    options: dict | None = None

# Specifies the type of format for batch requests:
class BatchFormat(BaseModel):
    tasks: list[TaskFormat]

# Defines the root page of the API:
@app.get("/")
def root():
    return{"message": "This is the root page. Please go to other page for further details."}

# Defines a page that specifies the health of the service/API:
@app.get("/health")
def health():
    return {"status": "all good"}

# Handles task processing requests:
@app.post("/task")
async def task(task: TaskFormat):
    raise NotImplementedError

# Handles batch requests for multiple tasks:
@app.post("/batch")
async def batch(tasklist):
    raise NotImplementedError

# Returns the task ID for the specified task:
@app.get("/task/{task_id}")
async def task_task_id():
    raise NotImplementedError
