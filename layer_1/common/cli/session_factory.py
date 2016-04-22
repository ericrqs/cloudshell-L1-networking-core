__author__ = 'g8y3e'

import importlib
from layer_1.common.configuration_parser import ConfigurationParser

class SessionFactory:
    @staticmethod
    def create(session_type):
        module = importlib.import_module('layer_1.common.cli.' + session_type + '_session')
        class_name = ConfigurationParser.get('cli_variable', session_type)
        if hasattr(module, class_name):
            return getattr(module, class_name)()

        return None
