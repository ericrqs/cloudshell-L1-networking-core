__author__ = 'g8y3e'

import importlib

import time
import os
from helper.system_helper import get_file_path

from layer_1.common.configuration_parser import ConfigurationParser
from layer_1.common.xml_wrapper import XMLWrapper

class RequestHandler:
    def __init__(self):
        self._driver_handler = None
        self._state_id = '-1'

        self._state_id_template = open(get_file_path('common/response_template/'
                                                     'state_id_template.xml')).read()
        self.init_driver_handler()

    def init_driver_handler(self):
        driver_module_data = ConfigurationParser.get('common_variable', 'driver_module')
        driver_module_name = driver_module_data[0]
        driver_class_name = driver_module_data[1]

        module = importlib.import_module(driver_module_name)
        if hasattr(module, driver_class_name):
            self._driver_handler = getattr(module, driver_class_name)()
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

    def set_state_id(self, command_node, xs_prefix=''):
        """
        <Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
            <Command CommandName="SetStateId" CommandId="29d2dd21-0a18-4c94-a43c-0f0e8f355151">
                <Parameters xsi:type="SetStateCommandParameters">
                    <StateId>635896045076120729</StateId>
                </Parameters>
            </Command>
        </Commands>

        :param command_node:
        :param xs_prefix:
        :return:
        """
        parameters_node = XMLWrapper.get_child_node(command_node, 'Parameters', xs_prefix)
        state_node = XMLWrapper.get_child_node(parameters_node, 'StateId', xs_prefix)

        self._state_id = XMLWrapper.get_node_text(state_node)

        return None

    def get_state_id(self, command_node, xs_prefix=''):
        """
        <Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
            <Command CommandName="GetStateId" CommandId="9d75a6b5-3d1d-4e65-b3ba-42d7344adaef">
                <Parameters xsi:type="GetStateCommandParameters"/>
            </Command>
        </Commands>

        :param command_node:
        :param xs_prefix:
        :return:
        """
        state_id_node = XMLWrapper.parse_xml(self._state_id_template)
        XMLWrapper.set_node_text(state_id_node, self._state_id)

        return state_id_node

    def map_bidi(self, command_node, xs_prefix=''):
        """
        <Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
            <Command CommandName="MapBidi" CommandId="c2a37eca-472f-4492-810e-cdc237a7c33a">
                <Parameters xsi:type="BiMappingCommandParameters">
                    <MapPort_A>192.168.28.223/91</MapPort_A>
                    <MapPort_B>192.168.28.223/10</MapPort_B>
                    <MappingGroupName/>
                </Parameters>
            </Command>
        </Commands>

        :param command_node:
        :param xs_prefix:
        :return:
        """

        parameters_node = XMLWrapper.get_child_node(command_node, 'Parameters', xs_prefix)

        src_port_node = XMLWrapper.get_child_node(parameters_node, 'MapPort_A', xs_prefix)
        dst_port_node = XMLWrapper.get_child_node(parameters_node, 'MapPort_B', xs_prefix)

        src_port_str = XMLWrapper.get_node_text(src_port_node)
        dst_port_str = XMLWrapper.get_node_text(dst_port_node)

        return self._driver_handler.map_bidi(src_port_str.split('/'), dst_port_str.split('/'))

    def map_clear_to(self, command_node, xs_prefix=''):
        """
        <Commands xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.qualisystems.com/ResourceManagement/DriverCommands.xsd">
            <Command CommandName="MapClearTo" CommandId="09cc9080-386b-4143-aaa0-a7211370304b">
                <Parameters xsi:type="MapClearToCommandParameters">
                    <SrcPort>192.168.28.223/2</SrcPort>
                    <DstPort>192.168.28.223/49</DstPort>
                </Parameters>
            </Command>
        </Commands>

       :param command_node:
       :param xs_prefix:
       :return:
       """

        parameters_node = XMLWrapper.get_child_node(command_node, 'Parameters', xs_prefix)

        src_port_node = XMLWrapper.get_child_node(parameters_node, 'SrcPort', xs_prefix)
        dst_port_node = XMLWrapper.get_child_node(parameters_node, 'DstPort', xs_prefix)

        src_port_str = XMLWrapper.get_node_text(src_port_node)
        dst_port_str = XMLWrapper.get_node_text(dst_port_node)

        return self._driver_handler.map_clear_to(src_port_str.split('/'), dst_port_str.split('/'))

