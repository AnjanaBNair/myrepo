# folder_with_greatest_number_of_files.py - Finds the folder in a directory tree that has the greatest number of files.

import os                           # For walk()
from pathlib import Path            # For path we are walking from

largest_file_num = 0
folder_with_largest_files = ''

# Walk through folders and files
for folders, sub_folder, files in os.walk(Path.home()):
    count = 0
    for file in files:
        count += 1

    if count > largest_file_num:
        largest_file_num = count
        folder_with_largest_files = str(folders)

print(folder_with_largest_files + ' has the largest number of files with ' + str(largest_file_num) + ' files')
