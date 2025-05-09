# Updated setup.py for py2app bundling with native sync library
from setuptools import setup, Extension

# If you want to build the sync extension as part of this setup, uncomment ext_modules and ensure sync.c is present
sync_ext = Extension(
    name="sync",
    sources=["sync.c"],                # only if building here
    extra_compile_args=["-fPIC"],
    extra_link_args=["-bundle", "-undefined", "dynamic_lookup"],
)

APP = ['main.py']
DATA_FILES = [
    'FitCSVTool.jar',   # Java splitter tool
    'libsync.so',       # Native library built in CI (or sync.so/dylib)
]

OPTIONS = {
    'argv_emulation': True,
    'includes': [
        'gui', 'sync', 'divider',
        'parser_fit', 'parser_kdf', 'writer_fit'
    ],
    'packages': [
        'fitparse', 'fitdecode', 'fit_tool', 'numpy'
    ],
    'resources': [
        'libsync.so',      # ensures the library is placed in Contents/Resources
    ],
    'plist': {
        'CFBundleName': 'PolarGarminSyncSplit',
        'CFBundleShortVersionString': '1.0',
        'CFBundleIdentifier': 'com.yourcompany.polargarmin',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    # ext_modules=[sync_ext],    # uncomment to build sync.c here
)
