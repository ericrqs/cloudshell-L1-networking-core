__author__ = 'g8y3e'

import socket
import re

from xml_wrapper import XMLWrapper

class RequestHandler:
    def __init__(self, buffer_size=1024):
        self._buffer_size = buffer_size
        self._connection_socket = None

        self._re_command_end = r'</Commands>'

        self._parsing_error_xml = XMLWrapper.parse_xml_from_file('common/response_template/parsing_error.xml')

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
                current_output = ''
                self._connection_socket.send(XMLWrapper.get_string_from_xml(self._parsing_error_xml))
