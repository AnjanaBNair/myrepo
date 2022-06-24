# selective_copy.py - Walks through a folder tree and searches for files with a certain
# file extension (such as .pdf or .jpg) and copies these files from whatever location they are in to a new folder.

import os
import shutil
from pathlib import Path

# Walk through and archive txt and py files
for folders, subfolder, files in os.walk(Path.home()):

    for file in files:
        if file.endswith('.pdf'):
            try:
                # Note: The destination folder must already exist, else a file would be created
                print('Copying %s in %s.' % (file, folders))
                shutil.copy(os.path.join(folders, file), Path.cwd() / 'copy_of_pdfs3')
            except shutil.SameFileError:
                continue

print('Done.')
