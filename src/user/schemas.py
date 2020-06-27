from marshmallow import fields, Schema, validate
from src.shared.enumerators import UserType


class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    type = fields.String(required=True, validate=validate.OneOf([UserType.USER.value, UserType.MACHINE.value]))


class ProfileSchema(Schema):
    name = fields.String(required=True)
