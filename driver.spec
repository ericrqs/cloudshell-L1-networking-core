# -*- mode: python -*-

block_cipher = None

data_files = [('configuration/configuration.json',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\configuration\\configuration.json',
               'DATA'),
              ('common/response_template/parsing_error.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\parsing_error.xml',
               'DATA'),
              ('common/response_template/command_not_found_error.xml',
               'E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver\\layer_1\\common\\response_template\\parsing_error.xml',
               'DATA')]

a = Analysis(['layer_1\\main.py'],
             pathex=['E:\\g8y3e\\work\\Quali_Systems\\projects\\git\\python-l1-driver'],
             binaries=None,
             datas=[],
             hiddenimports=[],
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
