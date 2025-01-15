from typing import Annotated

from fastapi import Depends
from starlette.requests import Request
from app.apps.internal.views.router import internel_router
from app.apps.tasks.services.tasks import TaskServise


@internel_router.get(path='/task/{task_id}')
async def get_task(request: Request, task_id: int, service: Annotated[TaskServise, Depends(TaskServise)]):
    return await TaskServise.get_id(task_id)
