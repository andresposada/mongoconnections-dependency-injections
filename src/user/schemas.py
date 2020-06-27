from marshmallow import fields, validate
from src.shared.enumerators import UserType
from src.shared.general_utils import GenericSchema


class UserSchema(GenericSchema):
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    type = fields.String(required=True, validate=validate.OneOf([UserType.USER.value, UserType.MACHINE.value]))


class ProfileSchema(GenericSchema):
    name = fields.String(required=True)
