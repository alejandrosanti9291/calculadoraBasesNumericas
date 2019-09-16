# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['calculadora_bases_numericas.py'],
             pathex=['C:\\Users\\Daniel Cardozo\\Dropbox\\INGENIERIA DE SISTEMAS\\03_SEMESTRE_VII\\CURSO_inteligencia_artificial(londoño)\\talleres\\calculadora_bases_num'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='calculadora_bases_numericas',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
