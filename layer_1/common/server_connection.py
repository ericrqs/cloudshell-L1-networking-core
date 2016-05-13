__author__ = 'g8y3e'

import socket
from thread import start_new_thread

from layer_1.common.configuration_parser import ConfigurationParser
from layer_1.common.logger.qs_logger import get_qs_logger

class ServerConnection:
    def __init__(self, host, port, request_manager, exe_folder_str):
        driver_name = ConfigurationParser.get("common_variable", "driver_name")

        self._xml_logger = get_qs_logger(log_group=driver_name,
                                         log_folder=exe_folder_str, log_file_prefix=driver_name + '_XML')

        self._command_logger = get_qs_logger(log_group=driver_name, log_file_prefix=driver_name + '_COMMANDS',
                                             format='%(asctime)s [%(levelname)s]: %(name)s %(module)s - '
                                                    '%(funcName)-20s %(message)s',
                                             log_folder=exe_folder_str)

        self._command_logger.info("Driver name: " + driver_name)
        self._command_logger.info("Driver host: " + host)
        self._command_logger.info("Driver port: " + str(port))

        self._is_running = True

        self._host = host
        self._port = port

        self._request_manager = request_manager

        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self._server_socket.bind((self._host, self._port))
        except socket.error as error_object:
            # log will be  here
            self._command_logger.error(str(error_object))
            raise Exception('ServerConnection', 'Can\'t bind host and port: ' + self._host + ':' + self._port + '!')

        self._server_socket.listen(100)

    def _get_accept_socket(self):
        return self._server_socket.accept()

    def set_running(self, is_running):
        self._is_running = is_running

    def start_listeninig(self):
        while self._is_running:
            connection_data = self._get_accept_socket()
            print "New connection id: " + str(connection_data[0].fileno())
            if connection_data is not None:
                connection_socket = connection_data[0]

                start_new_thread(self._request_manager.parse_request, (connection_socket, self._xml_logger,
                                                                       self._command_logger))
