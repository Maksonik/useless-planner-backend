from fastapi.routing import APIRouter

from app.apps.internal.views.router import internel_router
from app.apps.tasks.views.router import tasks_router

main_router = APIRouter(prefix='')

main_router.include_router(internel_router, prefix="/internel")
main_router.include_router(tasks_router, prefix="/tasks")

