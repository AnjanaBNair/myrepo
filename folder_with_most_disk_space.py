# folder_with_most_disk_space.py - Finds the folder that uses the most disk space.

import os                       # For walk()
from pathlib import Path        # For path we are walking from

folder_with_largest_space = 0
folder_with_largest_space_name = ''

# Walk through folders and files
for folders, sub_folder, files in os.walk(Path.home()):
    file_size = 0

    # Add file sizes of each folder
    for file in files:
        try:
            file_size += os.path.getsize(os.path.join(folders, file))
        except FileNotFoundError:
            continue

    if file_size > folder_with_largest_space:
        folder_with_largest_space = file_size
        folder_with_largest_space_name = str(folders)

print(folder_with_largest_space_name + ' has the largest size of ' + str(folder_with_largest_space) + ' bytes')
