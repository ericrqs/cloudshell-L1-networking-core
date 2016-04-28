__author__ = 'g8y3e'

import importlib

from layer_1.common.configuration_parser import ConfigurationParser
from layer_1.common.xml_wrapper import XMLWrapper

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

    def login(self, command_node, xs_prefix=''):
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
        parameters_node = XMLWrapper.get_child_node(command_node, 'Parameters', xs_prefix)
        address_node = XMLWrapper.get_child_node(parameters_node, 'Address', xs_prefix)
        user_node = XMLWrapper.get_child_node(parameters_node, 'User', xs_prefix)
        password_node = XMLWrapper.get_child_node(parameters_node, 'Password', xs_prefix)

        address_str = XMLWrapper.get_node_text(address_node)
        user_str = XMLWrapper.get_node_text(user_node)
        password_str = XMLWrapper.get_node_text(password_node)

        return self._driver_handler.login(address_str, user_str, password_str)

    def get_resource_description(self, command_node, xs_prefix=''):
        """
        <Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
            <Command CommandName="GetResourceDescription" CommandId="0d7000f2-dc20-401a-bdc6-09a2e1cb1f02">
                <Parameters xsi:type="GetResourceDescriptionParameters">
                    <Address>192.168.28.223</Address>
                </Parameters>
            </Command>
        </Commands>

        :param command_node:
        :return:
        """
        parameters_node = XMLWrapper.get_child_node(command_node, 'Parameters', xs_prefix)

        address_node = XMLWrapper.get_child_node(parameters_node, 'Address', xs_prefix)
        address_str = XMLWrapper.get_node_text(address_node)

        return self._driver_handler.get_resource_description(address_str)