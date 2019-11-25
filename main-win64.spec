# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[
                '.',
                'C:\\Users\\jacques\\Anaconda3\\envs\\condaenv\\Library\\plugins\\platforms'
            ],
             binaries=[(
                'C:\\Users\\jacques\\Anaconda3\\envs\\condaenv\\Library\\plugins\\platforms',
                'platforms'
                ),
                ('.\\build\\lib.win-amd64-3.7\\GUI.cp37-win_amd64.pyd', '.'),
                ('.\\build\\lib.win-amd64-3.7\\solver.cp37-win_amd64.pyd', '.')
                ],
             datas=[],
             hiddenimports=[
                'PySide2',
                'PySide2.QtGui',
                'PySide2.QtCore',
                'PySide2.QtWidgets',
                'numpy',
                'scipy.optimize'
                ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
