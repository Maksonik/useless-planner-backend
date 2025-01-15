from typing import Union

from fastapi import FastAPI

from app.core.router import main_router

app = FastAPI()
app.include_router(main_router)
