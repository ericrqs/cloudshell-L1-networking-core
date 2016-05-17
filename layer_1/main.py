__author__ = 'g8y3e'

import sys
import os

from layer_1.common.configuration_parser import ConfigurationParser
from layer_1.common.server_connection import ServerConnection
from layer_1.common.request_manager import RequestManager
from layer_1.common.request_handler import RequestHandler
from layer_1.common.helper.system_helper import get_file_folder

import layer_1.common.request_handler as request_handler

if __name__ == '__main__':
    print 'Argument List: ', str(sys.argv)

    host = '0.0.0.0'
    port = 1024
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    exe_folder_str = get_file_folder(sys.argv[0])
    ConfigurationParser.set_root_folder(exe_folder_str)

    request_handler = RequestHandler()

    request_manager = RequestManager()
    request_manager.bind_command('login', (RequestHandler.login, request_handler))
    request_manager.bind_command('getresourcedescription', (RequestHandler.get_resource_description, request_handler))
    request_manager.bind_command('setstateid', (RequestHandler.set_state_id, request_handler))
    request_manager.bind_command('getstateid', (RequestHandler.get_state_id, request_handler))
    request_manager.bind_command('mapbidi', (RequestHandler.map_bidi, request_handler))
    request_manager.bind_command('mapclearto', (RequestHandler.map_clear_to, request_handler))
    request_manager.bind_command('mapclear', (RequestHandler.map_clear, request_handler))

    server_connection = ServerConnection(host, port, request_manager, exe_folder_str)

    server_connection.start_listeninig()


