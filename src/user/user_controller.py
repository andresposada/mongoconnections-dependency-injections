import json
from src.user.use_cases import UserUseCase
from src.user.schemas import UserSchema
from abc import ABC, abstractmethod

user_schema = UserSchema()


class UserControllerBase(ABC):

    def __init__(self, user_use_case: UserUseCase):
        self.user_use_case = user_use_case

    @abstractmethod
    def execute(self, **kwargs):
        pass


class UserControllerPost(UserControllerBase):

    def execute(self, **kwargs):
        user_json = json.loads(kwargs.get('data', {}))
        user_data = user_schema.load(user_json)
        return self.user_use_case.create_user(user_json=user_data)


class UserControllerDelete(UserControllerBase):

    def execute(self, **kwargs):
        user_id = kwargs.get('user_id', None)
        self.user_use_case.delete_user(user_id)
