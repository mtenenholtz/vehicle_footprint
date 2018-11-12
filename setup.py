import sys
import os
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = 'Console'
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['numpy.core._methods',
                     'numpy.lib.format',
                     'matplotlib.backends.backend_tkagg',
                    ],
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')
         ],
    },
}

executables = [
    Executable('corner_detection.py', base=base)
]

setup(name='corner_detection',
      version='0.1',
      description='Distance measuring tool',
      executables=executables,
      options=options
      )
