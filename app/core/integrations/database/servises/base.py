from abc import ABC, abstractmethod

from app.core.integrations.database.repositories.base import BaseRepository


class BaseService(ABC):
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    @abstractmethod
    def get_id(self, id_: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, id_: int):
        pass

    @abstractmethod
    def delete(self, id_: int):
        pass
    
    @abstractmethod
    def update(self, id_: int):
        pass
