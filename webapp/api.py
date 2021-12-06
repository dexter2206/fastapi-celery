from celery.result import AsyncResult
from fastapi import FastAPI
from models import TaskCreated, TaskDefinition, TaskResult
from worker import celery, create_task

app = FastAPI()


@app.post("/tasks", response_model=TaskCreated)
def schedule_task(payload: TaskDefinition) -> TaskCreated:
    task = create_task.delay(payload.x)
    return TaskCreated(task_id=task.id)


@app.get("/tasks/{task_id}", response_model=TaskResult)
def fetch_task_status(task_id: str) -> TaskResult:
    result = AsyncResult(task_id, app=celery)
    return TaskResult(task_id=task_id, result=result.result, status=result.status)
