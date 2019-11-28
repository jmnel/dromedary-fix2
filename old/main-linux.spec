# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.spec'],
             pathex=['C:\\Users\\jacques\\repos\\jmnel\\dromedary-fix2'],
             binaries=[],
             datas=[],
             hiddenimports=['PySide2', 
                            'PySide2.QtWidgets', 
                            'PySide2.QtCore', 
                            'PySide2.QtGui'],
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
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , resources=['build\\\\lib.win-amd64-3.7\\\\GUI.cp37-win_amd64.pyd', 'build\\\\lib.win-amd64-3.7\\\\solver.cp37-win_amd64.pyd'])
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
