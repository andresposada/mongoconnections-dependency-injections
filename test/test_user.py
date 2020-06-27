import unittest
import marshmallow
import json
import random
import string

import src.lambda_handler as handler
from src.user.schemas import UserSchema
from src.shared.enumerators import UserType
from src.containers import Controllers


class TestUser(unittest.TestCase):
    user_json = dict()
    user_bad_json = dict()
    user_schema = UserSchema()
    user_id = None

    def setUp(self) -> None:
        self.user_json = {
            'username': self.randString(5, False),
            'password': self.randString(10, True),
            'type': UserType.USER.value
        }
        self.user_bad_json = {
            'username': self.randString(5, False),
            'password': self.randString(10, True),
        }

    def tearDown(self) -> None:
        if self.user_id:
            delete_controller = Controllers.user_factory('user_controller_delete')
            delete_controller.execute(user_id=self.user_id)

    def randString(self, length=5, all_letters=True):
        your_letters = string.ascii_letters if all_letters else 'abcdefghi'
        return ''.join((random.choice(your_letters) for i in range(length)))

    def test_create_user_success(self):
        raw_json = json.dumps(self.user_json)
        event = {'json': raw_json}
        response = handler.lambda_handler(event, None)
        self.user_id = response.get('id')
        self.assertIsNotNone(response.get('id'))

    def test_create_user_failed(self):
        try:
            raw_json = json.dumps(self.user_bad_json)
            event = {'json': raw_json}
            response = handler.lambda_handler(event, None)
            self.fail('Should return an exception!!')
        except marshmallow.exceptions.ValidationError as e:
            self.assertIsNotNone(e)


if __name__ == '__main__':
    unittest.main()
