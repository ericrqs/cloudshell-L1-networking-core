__author__ = 'g8y3e'

from distutils.core import setup
import py2exe, sys, os

setup(name="<layer_1_driver>",
      version="1.0",
      description="L1 Diver",
      author="g8y3e",
      options={'py2exe': {
          'bundle_files': 1,
          'compressed': True,
          'includes': []
      }},
      console=[{'script': 'layer_1/main.py',
                'dest_base': 'app_name',
                'icon_resources': [(0, 'img/icon.ico')],
                'other_resources': []
                }])