# add_prefix_to_filename.py -  Adds a prefix to the start of the filename
# Such as adding spam_ to rename eggs.txt to spam_eggs.txt

import shutil
import os
from pathlib import Path        # For the third alternative

# FIRST ALTERNATIVE
for file in os.listdir('.'):
    if file.endswith('.txt'):

        # Get file path
        new_file_name = os.getcwd() + '/' + ('prefixed_' + file)
        file = os.getcwd() + '/' + file

        print('Changing %s to %s' % (file, new_file_name))

        # If you are happy with the changes printed out, uncomment the code line to effect changes
        # shutil.move(file, new_file_name)
print('Done.')

# SECOND ALTERNATIVE
"""
for file in os.listdir('.'):
    if file.endswith('.txt'):
        
        # Get file path
        abs_working_dir = os.path.abspath('.')
        new_file_name = os.path.join(abs_working_dir, ('prefixed_' + file))
        file = os.path.join(abs_working_dir, file)
        
        print('Changing %s to %s' % (file, new_file_name))
        
        # If you are happy with the changes printed out, uncomment the code line to effect changes
        # shutil.move(file, new_file_name)

print('Done.')
"""

# THIRD ALTERNATIVE
"""
for file in Path.cwd().glob('*.txt'):

    # Get file path
    # file.stem - file name; file.suffix - extension (.txt)
    new_file_name = Path.cwd() / ('prefixed_' + file.stem + file.suffix)

    print('Changing %s to %s' % (file, new_file_name))

    # If you are happy with the changes printed out, uncomment the code line to effect changes
    # shutil.move(file, new_file_name)

print('Done.')
"""
