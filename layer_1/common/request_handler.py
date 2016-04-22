__author__ = 'g8y3e'

import importlib

from layer_1.common.configuration_parser import ConfigurationParser

class RequestHandler:
    def __init__(self):
        self.init_driver_handler()

    def init_driver_handler(self):
        driver_folder = ConfigurationParser.get('common_variable', 'driver_folder_name')
        module = importlib.import_module('layer_1.' + driver_folder + '.' + driver_folder + '_driver_handler')
        handler_name = ConfigurationParser.get('common_variable', 'driver_handler_name')

        if hasattr(module, handler_name):
            self._driver_handler = getattr(module, handler_name)()
            return

        raise Exception('RequestHandler', 'Can\'t found class in package!')

    def login(self, xml_node):
        """
        <Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
            <Command CommandName="Login" CommandId="567f4dc1-e2e5-4980-b726-a5d906c8679b">
                <Parameters xsi:type="LoginCommandParameters">
                    <Address>192.168.28.223</Address>00
                    <User>root</User>
                    <Password>root</Password>
                </Parameters>
            </Command>
        </Commands>

        :param xml_node:
        :return:
        """
        self._driver_handler.login('<ip>', 'admin', 'password')
