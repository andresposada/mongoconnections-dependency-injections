from abc import ABC, abstractmethod

from src.user.domain import UserEntity


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        pass
