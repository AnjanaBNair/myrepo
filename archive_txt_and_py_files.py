# archive_txt_and_py_files.py - Walk a directory tree and archive files with .txt or .py extensions.

import os
import zipfile
from pathlib import Path

txt_py_zip = zipfile.ZipFile('txt_py_archive.zip', 'w')

# Walk through and archive txt and py files
for folders, subfolder, files in os.walk(Path.home()):

    for file in files:
        if file.endswith('.txt') or file.endswith('.py'):
            print('Adding %s in %s.' % (file, folders))
            txt_py_zip.write(os.path.join(folders, file))

print('Done.')
