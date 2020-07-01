from enum import Enum


class UserType(Enum):
    MACHINE = 'MACHINE'
    USER = 'USER'


class Constant(Enum):
    BASE_CONFIG_PATH = 'resources/application-{}.yml'
