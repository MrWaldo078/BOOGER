# Updated setup.py for py2app bundling with native sync library (C++ version)
from setuptools import setup, Extension

# Build the C++ sync extension as part of this setup
sync_ext = Extension(
    name="sync",
    sources=["sync.cpp"],        # C++ source file in BOOGER directory
    extra_compile_args=["-fPIC", "-std=c++11"],
    extra_link_args=["-bundle", "-undefined", "dynamic_lookup"],
    language="c++",
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
    install_requires=[],
    setup_requires=[
        'py2app',
        'jaraco.text>=4.0',
    ],
    setup_requires=['py2app'],
    ext_modules=[sync_ext],
)
