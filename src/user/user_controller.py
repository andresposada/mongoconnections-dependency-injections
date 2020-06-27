import json
from src.user.use_cases import UserUseCase
from src.user.schemas import UserSchema
from abc import ABC, abstractmethod
from src.containers import Services


class UserControllerBase(ABC):

    @abstractmethod
    def execute(self, **kwargs):
        pass


class UserControllerPost(UserControllerBase):

    def execute(self, **kwargs):
        user_service = Services.user_service
        user_service.create_user()


class UserController:

    @staticmethod
    def post(event, context):
        user_json = json.loads(event['json'])
        user_schema = UserSchema()
        user_data = user_schema.load(user_json)
        UserUseCase.create_user(user_data)
