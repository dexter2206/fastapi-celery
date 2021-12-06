from celery.result import AsyncResult
from fastapi import FastAPI
from models import TaskCreated, TaskDefinition, TaskResult
from worker import celery, square

app = FastAPI()


@app.post("/tasks", response_model=TaskCreated)
def schedule_task(payload: TaskDefinition) -> TaskCreated:
    """Schedule computing of x ** 2."""
    task = square.delay(payload.x)
    return TaskCreated(task_id=task.id)


@app.get("/tasks/{task_id}", response_model=TaskResult)
def fetch_task_status(task_id: str) -> TaskResult:
    """Fetch status of given task and (if available) its result."""
    result = AsyncResult(task_id, app=celery)
    return TaskResult(task_id=task_id, result=result.result, status=result.status)
