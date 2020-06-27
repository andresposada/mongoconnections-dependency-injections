import json
import src.containers as containers


def lambda_handler(event, context):
    user_json = json.loads(event['json'])
    user_controller = containers.Controllers.user_factory('user_controller_post')
    user_controller.execute(user_json)
