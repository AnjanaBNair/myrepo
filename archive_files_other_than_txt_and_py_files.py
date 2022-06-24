# archive_files_other_than_txt_and_py_files.py - Walk a directory tree and archive every file 
# except files with .txt and .py extensions.

import os
import zipfile
from pathlib import Path

files_zip = zipfile.ZipFile('files_archive.zip', 'w')

# Walk through and archive files other than txt and py files
for folders, sub_folders, files in os.walk(Path.home()):
    for file in files:
        try:

            if file.endswith('.txt') or file.endswith('.py'):
                continue

            print('Adding %s in %s.' % (file, folders))
            files_zip.write(os.path.join(folders, file))

        # Files requiring permission won't be added to the zip file.
        except PermissionError:
            print(str(os.path.join(folders, file)) + ' requires permission!')
            continue
print('Done.')
