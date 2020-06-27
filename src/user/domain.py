from src.shared.utils import get_hashed_password
from src.shared.general_utils import GeneralEntity
import mongoengine as me
from src.shared.enumerators import UserType


class UserEntity(GeneralEntity):
    meta = {'collection': 'User'}
    username = me.StringField(required=True, max_length=30)
    password = me.StringField(required=True, max_length=100)
    type = me.StringField(required=True, max_length=10, choices=[UserType.MACHINE.value, UserType.USER.value])

    def clean(self):
        self.password = get_hashed_password(self.password)
        super().clean()
