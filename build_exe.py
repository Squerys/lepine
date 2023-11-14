from beta import *

import PyInstaller.__main__


def build(name):
    PyInstaller.__main__.run([
    'lepine_client.py',
    '--onefile',
    '--name', name
    ])


