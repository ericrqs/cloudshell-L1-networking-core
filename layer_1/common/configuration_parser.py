__author__ = 'g8y3e'

import os
import sys
import json

from helper.system_helper import get_file_path

class ConfigurationParser:
    _CONFIG_JSON = None
    _RUNTIME_CONFIG_JSON = None
    _CONFIG_PATH = "configuration/configuration.json"
    _ROOT_FOLDER = None

    @staticmethod
    def set_root_folder(folder_path):
        ConfigurationParser._ROOT_FOLDER = folder_path

    @staticmethod
    def init():
        if ConfigurationParser._CONFIG_JSON is None:
            configure_path = ConfigurationParser._CONFIG_PATH
            json_data = open(get_file_path(configure_path)).read()
            ConfigurationParser._CONFIG_JSON = json.loads(json_data)

        if ConfigurationParser._RUNTIME_CONFIG_JSON is None:
            configure_path = ConfigurationParser._ROOT_FOLDER + \
                             ConfigurationParser._CONFIG_JSON["common_variable"]["runtime_configuration"]
            json_data = open(configure_path).read()
            ConfigurationParser._RUNTIME_CONFIG_JSON = json.loads(json_data)

    @staticmethod
    def get(*args):
        ConfigurationParser.init()

        result_data = ConfigurationParser._RUNTIME_CONFIG_JSON
        founded = True
        for key in args:
            if (isinstance(result_data, list) and key < len(result_data)) or \
                    (isinstance(result_data, dict) and key in result_data):
                result_data = result_data[key]
            else:
                founded = False
                break

        if founded:
            return result_data

        result_data = ConfigurationParser._CONFIG_JSON
        for key in args:
            if (isinstance(result_data, list) and key < len(result_data)) or \
                    (isinstance(result_data, dict) and key in result_data):
                result_data = result_data[key]
            else:
                return None

        return result_data
