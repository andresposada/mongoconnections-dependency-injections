import collections
import json

from mongoengine import connect

import src.containers as containers
from dependency_injector import providers
from src.shared.enumerators import Constant
from src.shared.config_singleton import ConfigSingleton
import dependency_injector.providers as providers
import src.shared.utils as utils
import os


def generate_configuration_source_name(context):
    # active_profile = utils.get_active_profile(context)
    active_profile = 'dev'
    return Constant.BASE_CONFIG_PATH.value.format(active_profile)


def lambda_handler(event, context):
    active_profile = 'dev'
    # config_file_path = generate_configuration_source_name(context)

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, f"resources/application-{active_profile}.yml")

    if not containers.Core.config.last_overriding:
        containers.Core.config.from_yaml(path)
        db = containers.Core.config.db
        connect(
            db.database(),
            host=db.host(),
            username=db.username(),
            password=db.password(),
            port=db.port(),
            authentication_source=db.authentication_source()
        )

    # containers.Gateways.mongo_connection

    user_controller = containers.Controllers.user_factory('user_controller_post')
    return user_controller.execute(data=event['json'])


def set_db_connection_if_necessary():
    DbConnectionService = collections.namedtuple('DbConnectionService', [])
    db_connection_provider = providers.Singleton(DbConnectionService)
    db_connection_service = db_connection_provider()
    db_connection_service()


def set_config_provider(context):
    config_provider = providers.Configuration()
    # active_profile = utils.get_active_profile(context)
    active_profile = 'dev'
    ConfigSingleton.get_instance().set_active_profile(active_profile)
    config_file_path = generate_configuration_source_name(active_profile)
    config_provider.from_yaml(config_file_path)
    ConfigSingleton.get_instance().set_config_provider(config_provider)


def generate_configuration_source_name(active_profile):
    return Constant.BASE_CONFIG_PATH.value.format(active_profile)
