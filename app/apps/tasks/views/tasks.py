from sqlalchemy import text
from starlette.requests import Request

from app.apps.tasks.views.router import tasks_router
from app.core.integrations.database.database import engine


@tasks_router.get(path='/tasks')
async def get_tasks(request: Request):
    pass

@tasks_router.get(path='/tasks/{task_id}')
async def get_task(request: Request, task_id: int):
    pass


@tasks_router.post(path='/tasks/{task_id}')
async def create_task(request: Request, task_id: int):
    pass


@tasks_router.delete(path='/tasks/{task_id}')
async def delete_task(request: Request, task_id: int):
    pass


@tasks_router.patch(path='/tasks/{task_id}')
async def patch_task(request: Request, task_id: int):
    pass