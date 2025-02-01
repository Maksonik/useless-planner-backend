from app.core.integrations.database.servises.sqlalchemy import SQLAlchemyService


class TaskRepository:
    pass


class TaskServise(SQLAlchemyService):
    def __init__(self, repository: TaskRepository):
        self.repository = repository
