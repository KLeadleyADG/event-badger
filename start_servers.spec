# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

# Node.js server files (correct paths)
node_server_files = [
    ('backend/node_server/config', 'backend/node_server/config'),
    ('backend/node_server/controllers', 'backend/node_server/controllers'),
    ('backend/node_server/middlewares', 'backend/node_server/middlewares'),
    ('backend/node_server/models', 'backend/node_server/models'),
    ('backend/node_server/routes', 'backend/node_server/routes'),
    ('backend/node_server/server.js', 'backend/node_server')
]

# Python backend files
python_datas = [
    ('backend/python_server', 'backend/python_server')
]

# Frontend files
frontend_files = [
    ('frontend', 'frontend'),
    ('.expo', '.expo'),
    ('babel.config.js', 'babel.config.js'),
    ('app.json', 'app.json')
]

# Shared Node.js modules
node_modules_files = [('node_modules', 'node_modules')]

# Environment and configuration files
env_files = [
    ('.env', '.env'),
    ('package.json', 'package.json'),
    ('package-lock.json', 'package-lock.json'),
]

# Combine all data files
datas = (
    python_datas +
    node_server_files +
    frontend_files +
    node_modules_files +
    env_files
)

# Hidden imports for Python standard library
hiddenimports = ['encodings', 'codecs']

# PyInstaller build configuration
a = Analysis(
    ['start_servers.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='start_servers',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Change to True if you want to see the console output
    icon='icon.ico'  # Ensure the icon file exists at the root level
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='start_servers'
)
