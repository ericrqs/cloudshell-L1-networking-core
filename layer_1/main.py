__author__ = 'g8y3e'

import sys

from layer_1.common.server_connection import ServerConnection
from layer_1.common.request_handler import RequestHandler

if __name__ == '__main__':
    print 'Argument List: ', str(sys.argv)

    host = '127.0.0.1'
    port = 1023
    if len(sys.argv) > 1:
        port = sys.argv[1]

    request_handler = RequestHandler()
    server_connection = ServerConnection(host, port, request_handler)

    server_connection.start_listeninig()


