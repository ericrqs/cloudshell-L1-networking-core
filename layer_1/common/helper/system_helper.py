__author__ = 'g8y3e'

import sys
import os

def get_file_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        relative_path = os.path.join(sys._MEIPASS, relative_path)
    else:
        relative_path = os.path.abspath(".") + os.sep + relative_path

    return relative_path
