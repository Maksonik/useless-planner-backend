from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/postgres", echo=True)