import json
import src.containers as containers


def lambda_handler(event, context):
    if 'user' in event.get('uri'):
        if 'POST' in event.get('method'):
            user_create_controller = containers.Controllers.user_factory('user_controller_post')
            return user_create_controller.execute(data=event['json'])
        elif 'DELETE' in event.get('method'):
            user_delete_controller = containers.Controllers.user_factory('user_controller_delete')
            return user_delete_controller.execute(data={'userId': event['header']['userId']})

