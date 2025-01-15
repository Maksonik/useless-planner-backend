from app.apps.internal.views.router import internel_router


@internel_router.get(path='/health_check')
async def health_check():
    return {"status": "200 ok"}
