__author__ = 'g8y3e'

import socket
import re

from xml_wrapper import XMLWrapper
from helper.system_helper import get_file_path

class RequestManager:
    def __init__(self, buffer_size=1024):
        self._buffer_size = buffer_size
        self._connection_socket = None
        self._request_handler = None

        self._commands_dict = dict()

        self._re_command_end = r'</Commands>'
        self._end_command = '\r\n'

        self._parsing_error_xml = XMLWrapper.parse_xml_from_file(get_file_path('common/response_template/'
                                                                               'parsing_error.xml'))

        self._command_response_data = open(get_file_path('common/response_template/'
                                                         'command_response_template.xml')).read()

        self._responses_data = open(get_file_path('common/response_template/'
                                                 'responses_template.xml')).read()

    def set_request_handler(self, request_handler):
        self._request_handler = request_handler

    def bind_command(self, command_name, callback_tuple):
        self._commands_dict[command_name] = callback_tuple

    def _set_response_error(self, responses_node, error_code, error_text, xs_prefix=None):
        XMLWrapper.set_node_attr(responses_node, 'Success', attr_value='false')

        if xs_prefix is None:
            xs_prefix = '{http://schemas.qualisystems.com/ResourceManagement/DriverCommandResult.xsd}'

        error_node = XMLWrapper.get_child_node(responses_node, 'ErrorCode', xs_prefix)
        XMLWrapper.set_node_text(error_node, error_code)

        log_node = XMLWrapper.get_child_node(responses_node, 'Log', xs_prefix)
        XMLWrapper.set_node_text(log_node, error_text)

        return responses_node

    def parse_request(self, connection_socket):
        self._connection_socket = connection_socket
        self._connection_socket.settimeout(60)

        current_output = ''
        while True:
            try:
                current_output += self._connection_socket.recv(self._buffer_size)
            except socket.timeout:
                continue
            except Exception as error_object:
                raise error_object

            match_result = re.search(self._re_command_end, current_output)
            if match_result:
                responses_node = XMLWrapper.parse_xml( self._responses_data)

                try:
                    request_node = XMLWrapper.parse_xml(current_output)
                except Exception as error_object:
                    responses_node = self._set_response_error(responses_node, '0',
                                                              'Failed to parse the xml')

                    self._connection_socket.send(XMLWrapper.get_string_from_xml(responses_node) +
                                                 self._end_command)
                    current_output = ''
                    continue

                xs_prefix = XMLWrapper.get_node_prefix(request_node, 'xsi')

                for command_node in request_node:
                    # get commands list
                    command_name = XMLWrapper.get_node_attr(command_node, 'CommandName')
                    command_id = XMLWrapper.get_node_attr(command_node, 'CommandId')

                    if command_name is not None:
                        command_name = command_name.lower()
                        if command_name in self._commands_dict:
                            callback_tuple = self._commands_dict[command_name]

                            command_response_node = XMLWrapper.parse_xml(self._command_response_data)

                            XMLWrapper.set_node_attr(command_response_node, 'CommandName', attr_value='Login')
                            XMLWrapper.set_node_attr(command_response_node, 'CommandId', attr_value=command_id)

                            return_state = True
                            try:
                                callback_tuple[0](callback_tuple[1], request_node)
                            except Exception as error_object:
                                return_state = False
                                self._set_response_error(responses_node, '0', '')

                            XMLWrapper.set_node_attr(command_response_node, 'Success',
                                                     attr_value=str(return_state).lower())

                            XMLWrapper.append_child(responses_node, command_response_node)
                        else:
                            responses_node = self._set_response_error(responses_node, '404',
                                                                      'Command not found!')

                self._connection_socket.send(XMLWrapper.get_string_from_xml(responses_node) + self._end_command)
