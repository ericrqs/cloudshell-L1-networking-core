__author__ = 'g8y3e'

from abc import abstractmethod

from configuration_parser import ConfigurationParser
from cli.session_factory import SessionFactory

class DriverHandlerBase:
    def __init__(self):
        connection_type = ConfigurationParser.get("common_variable", "connection_type")

        self._session = SessionFactory.create(connection_type)
        self._prompt = ConfigurationParser.get("common_variable", "device_prompt")

    @abstractmethod
    def login(self, address, username, password):
        pass

    @abstractmethod
    def get_resource_description(self, address):
        pass
