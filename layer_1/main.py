__author__ = 'g8y3e'

import sys

from layer_1.common.server_connection import ServerConnection
from layer_1.common.request_manager import RequestManager

import layer_1.common.request_handler as request_handler

if __name__ == '__main__':
    print 'Argument List: ', str(sys.argv)

    host = '127.0.0.1'
    port = 1023
    if len(sys.argv) > 1:
        port = sys.argv[1]

    request_manager = RequestManager()
    request_manager.bind_command('login', request_handler.login)

    server_connection = ServerConnection(host, port, request_handler)

    server_connection.start_listeninig()


