__author__ = 'g8y3e'

import sys
import os

def get_file_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        relative_path = os.path.join(sys._MEIPASS, relative_path)
    else:
        relative_path = os.path.abspath(".") + os.sep + relative_path

    return relative_path

def get_file_folder(file_path):
    index = file_path.rfind('\\')
    file_folder = ''
    if index != -1:
        file_folder = file_path[:index + 1]
    else:
        index = file_path.rfind('/')
        if index != -1:
            file_folder = file_path[:index + 1]

    return file_folder