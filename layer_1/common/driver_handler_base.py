__author__ = 'g8y3e'

from abc import abstractmethod

class DriverHandlerBase:
    @abstractmethod
    def login(self, address, username, password):
        pass
