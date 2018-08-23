# -*- mode: python -*-

block_cipher = None


a = Analysis(['fracMorse.py'],
             pathex=['/Users/piercewang/Documents/Projects/Morse Code/fractionatedMorse/src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='fracMorse',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='fracMorse.app',
             icon=None,
             bundle_identifier=None)
