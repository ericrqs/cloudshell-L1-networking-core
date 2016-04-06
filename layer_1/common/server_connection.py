__author__ = 'g8y3e'

import socket
from thread import start_new_thread

class ServerConnection:
    def __init__(self, host, port, request_manager):
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
                start_new_thread(self._request_manager.parse_request, (connection_socket, ))
