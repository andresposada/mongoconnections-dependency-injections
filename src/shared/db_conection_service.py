from mongoengine import connect
from src.shared.config_singleton import ConfigSingleton


class DbConnectionService:

    def __init__(self):
        config = ConfigSingleton.get_instance().get_config_provider()
        connect(
            'loto-db-connection',
            db=config.db.database(),
            username=config.db.username(),
            password=config.db.password(),
            host=config.db.host()
        )

