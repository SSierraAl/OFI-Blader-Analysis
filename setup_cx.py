import sys
from cx_Freeze import setup, Executable

includes = ['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets',
            'PySide6.QtWebEngineWidgets', 'PySide6.QtSvgWidgets']

# Include your files and folders
includefiles = ['gui/', 'settings.json', 'qt_core.py', 'icon.ico']

# Exclude unnecessary packages
excludes = ['cx_Freeze']

base = "Win32GUI"
shortcutName = None
shortcutDir = None
icon = "icon.ico"
if sys.platform == "win32":
    base = "Win32GUI"
    shortcutName = 'My App'
    shortcutDir = "DesktopFolder"

setup(
    name='LaserApp',
    version='0.1',
    author='Oasis',
    author_email='',
    options={'build_exe': {
        'includes': includes,
        'excludes': excludes,
        'include_files': includefiles}
        },
    executables=[Executable('main.py',
                            base=base,
                            icon="icon.ico"),
                 ]
)

### Linux Version ###

"""
import sys
from cx_Freeze import setup, Executable

includes = ['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets',
            'PySide6.QtWebEngineWidgets', 'PySide6.QtSvgWidgets']

# Include your files and folders
includefiles = ['gui/', 'settings.json', 'qt_core.py', 'icon.ico']

# Exclude unnecessary packages
excludes = ['cx_Freeze']

base = none
shortcutName = None
shortcutDir = None
icon = "icon.ico"
if sys.platform == "win32":
    base = "Win32GUI"
    shortcutName = 'My App'
    shortcutDir = "DesktopFolder"

setup(
    name='LaserApp',
    version='0.1',
    author='Oasis',
    author_email='',
    options={'build_exe': {
        'includes': includes,
        'excludes': excludes,
        'include_files': includefiles}
        },
    executables=[Executable('main.py',
                            base=base,
                            icon="icon.ico"),
                 ]
)
"""