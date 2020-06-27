import unittest
import marshmallow

from src.user.mongo_repository import UserMongoRepository
from src.user.schemas import UserSchema
from src.shared.enumerators import UserType
from src.user.use_cases import UserUseCase


class TestUser(unittest.TestCase):
    user_json = dict()
    user_bad_json = dict()

    def setUp(self) -> None:
        self.user_json = {
            'username': 'afp',
            'password': '123456',
            'type': UserType.USER.value
        }
        self.user_bad_json = {
            'username': 'ccc',
            'password': '123456',
        }

    def tearDown(self) -> None:
        pass

    def test_save_user(self):
        user_schema = UserSchema()
        data = user_schema.load(self.user_json)
        user_case = UserUseCase(UserMongoRepository())
        ret_schema = user_case.create_user(data)
        self.assertEqual(ret_schema['username'], data['username'])

    def test_save_failed_user(self):
        user_schema = UserSchema()
        try:
            data = user_schema.load(self.user_bad_json)
            user_case = UserUseCase(UserMongoRepository())
            user_case.create_user(data)
            self.fail('Should return an exception!!')
        except marshmallow.exceptions.ValidationError as e:
            self.assertIsNotNone(e)


if __name__ == '__main__':
    unittest.main()
