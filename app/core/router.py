from fastapi.routing import APIRouter

from app.apps.internal.views.router import internel_router

main_router = APIRouter(prefix='')

main_router.include_router(internel_router, prefix="/internel")

