# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[
                '.'
            ],
             binaries=[
                ( './build/lib.linux-x86_64-3.7/solver.cpython-37m-x86_64-linux-gnu.so', '.'),
                ( './build/lib.linux-x86_64-3.7/GUI.cpython-37m-x86_64-linux-gnu.so', '.')
                ],
             datas=[],
             hiddenimports=[
                'PySide2',
                'PySide2.QtGui',
                'PySide2.QtCore',
                'PySide2.QtWidgets',
                'numpy',
                'scipy.optimize',
                'six'
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
