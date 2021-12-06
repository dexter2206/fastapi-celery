from typing import Optional

from pydantic import BaseModel, PositiveFloat


class TaskDefinition(BaseModel):
    """Body accepted by POST /tasks"""

    x: PositiveFloat  # We require x to be positive, since we use it for sleeping


class TaskCreated(BaseModel):
    """Response returned from POST /tasks"""

    task_id: str


class TaskResult(BaseModel):
    """Response returned from GET /tasks/{task_id}"""

    task_id: str
    status: str
    result: Optional[float]
