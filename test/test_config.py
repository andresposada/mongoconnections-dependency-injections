import unittest
from dependency_injector import providers
from src.shared.enumerators import Constant
from src.shared.config_singleton import ConfigSingleton


class TestUser(unittest.TestCase):
    active_profile = 'dev'

    def setUp(self) -> None:
        config_provider = providers.Configuration()
        config_file_path = self.generate_configuration_source_name()
        config_provider.from_yaml(config_file_path)
        ConfigSingleton.get_instance().set_config_provider(config_provider)

    def tearDown(self) -> None:
        pass

    def generate_configuration_source_name(self):
        return Constant.BASE_CONFIG_PATH.value.format(self.active_profile)

    def test_profile_configuration(self):
        config_provider = ConfigSingleton.get_instance().get_config_provider()
        assert config_provider() == {'aws': {'access_key_id': 'TESTKEY1234', 'secret_access_key': 'TESECRET$%^&'}}
        assert config_provider.aws() == {'access_key_id': 'TESTKEY1234', 'secret_access_key': 'TESECRET$%^&'}
        assert config_provider.aws.access_key_id() == 'TESTKEY1234'
        assert config_provider.aws.secret_access_key() == 'TESECRET$%^&'


if __name__ == '__main__':
    unittest.main()
