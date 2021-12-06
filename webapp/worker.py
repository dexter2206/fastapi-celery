import os
import time

from celery import Celery

# Following Twelve-factor app methodology, we store configuration in env variables
celery = Celery(
    __name__,
    broker=os.environ.get("BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("RESULT_BACKEND", "redis://localhost:6379"),
)


@celery.task(name="create_task")
def create_task(x: float) -> float:
    """Compute x ** 2 after sleeping for x seconds."""
    time.sleep(x)
    return x ** 2
