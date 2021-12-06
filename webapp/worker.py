import os
import time

from celery import Celery

celery = Celery(
    __name__,
    broker=os.environ.get("BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("RESULT_BACKEND", "redis://localhost:6379"),
)


@celery.task(name="create_task")
def create_task(x):
    time.sleep(x)
    return x ** 2
