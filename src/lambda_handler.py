import json
import src.containers as containers


def lambda_handler(event, context):
    user_controller = containers.Controllers.user_factory('user_controller_post')
    return user_controller.execute(data=event['json'])
