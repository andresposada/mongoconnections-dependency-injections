from src.user.domain import UserEntity
from src.user.repository import UserRepository


class UserMongoRepository(UserRepository):

    def save(self, user: UserEntity) -> UserEntity:
        return user.save()
