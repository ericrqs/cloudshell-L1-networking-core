# -*- mode: python -*-

block_cipher = None

data_files = [('configuration/configuration.json',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\configuration\\configuration.json',
               'DATA'),
              ('common/response_template/parsing_error.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\parsing_error.xml',
               'DATA'),
              ('common/response_template/resource_incoming_map_template.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\resource_incoming_map_template.xml',
               'DATA'),
              ('common/response_template/resource_template.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\resource_template.xml',
               'DATA'),
              ('common/response_template/responses_template.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\responses_template.xml',
               'DATA'),
              ('common/response_template/command_response_template.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\command_response_template.xml',
               'DATA'),
              ('common/response_template/resource_attribute_template.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\resource_attribute_template.xml',
               'DATA'),
               ('common/response_template/state_id_template.xml',
                'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\state_id_template.xml',
                'DATA'),
               ('common/logger/qs_config.ini',
                'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\logger\\qs_config.ini',
                'DATA')]

a = Analysis(['layer_1\\main.py'],
             pathex=['E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver'],
             binaries=None,
             datas=[],
             hiddenimports=[
                "layer_1.common.cli.tcp_session",
                "layer_1.common.cli.telnet_session",
                "layer_1.common.cli.console_session",
                "layer_1.common.cli.ssh_session",

                "layer_1.polatis.polatis_driver_handler"
             ],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries + data_files,
          a.zipfiles,
          a.datas,
          name='driver_name',
          debug=False,
          strip=None,
          upx=True,
          console=True , version='version.txt', icon='img\\icon.ico')
