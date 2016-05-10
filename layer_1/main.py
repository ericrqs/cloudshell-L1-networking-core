__author__ = 'g8y3e'

import sys
import os

from layer_1.common.configuration_parser import ConfigurationParser
from layer_1.common.server_connection import ServerConnection
from layer_1.common.request_manager import RequestManager
from layer_1.common.request_handler import RequestHandler

import layer_1.common.request_handler as request_handler

if __name__ == '__main__':
    print 'Argument List: ', str(sys.argv)

    host = '0.0.0.0'
    port = 1024
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    request_handler = RequestHandler()

    request_manager = RequestManager()
    request_manager.bind_command('login', (RequestHandler.login, request_handler))
    request_manager.bind_command('getresourcedescription', (RequestHandler.get_resource_description, request_handler))
    request_manager.bind_command('setstateid', (RequestHandler.set_state_id, request_handler))
    request_manager.bind_command('getstateid', (RequestHandler.get_state_id, request_handler))
    request_manager.bind_command('mapbidi', (RequestHandler.map_bidi, request_handler))
    request_manager.bind_command('mapclearto', (RequestHandler.map_clear_to, request_handler))

    exe_folder_str = sys.argv[0]
    index = exe_folder_str.rfind('\\')
    if index != -1:
        exe_folder_str = exe_folder_str[:index + 1]
    else:
        index = exe_folder_str.rfind('/')
        if index != -1:
            exe_folder_str = exe_folder_str[:index + 1]

    print exe_folder_str

    server_connection = ServerConnection(host, port, request_manager, exe_folder_str)

    server_connection.start_listeninig()


