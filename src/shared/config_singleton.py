""" Singleton class for parameter store management in efactura aggregator lambda function"""


class ConfigSingleton:
    __instance = None
    __config_provider = None

    @classmethod
    def get_instance(cls):
        """
        Gets the class instance
        :return:
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def get_config_provider(self):
        """
        Gets the configuration provider
        :return:
        """
        return self.__config_provider

    def set_config_provider(self, config_provider):
        """
        Sets the current config provider value
        @param config_provider:
        """
        self.__config_provider = config_provider