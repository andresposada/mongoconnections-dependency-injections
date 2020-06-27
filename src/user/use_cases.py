from src.user.schemas import UserSchema
from src.user.domain import UserEntity
from src.user.repository import UserRepository


class UserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_json: dict) -> dict:
        user = UserEntity(**user_json)
        saved_user = self.user_repository.save(user)
        ret_schema = UserSchema()
        return ret_schema.dump(saved_user)
