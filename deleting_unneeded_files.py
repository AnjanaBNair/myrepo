# deleting_unneeded_files.py - Find files that use the most disk space to know which files to delete.

import os                       # For walk()
from pathlib import Path        # For path we are walking from

file_100mb_and_above = {}       # Files that are 100 mb or above
hundred_mb = 104857600

# Walk through folders and files
for folders, sub_folder, files in os.walk(Path.home()):
    file_size = 0

    # Find files of 100 MB and above.
    for file in files:
        try:
            file_size = os.path.getsize(os.path.join(folders, file))

            # Add files of 100 MB and above
            if file_size >= hundred_mb:
                file_100mb_and_above[file] = '%s MB' % (round(file_size / 1048576, 2))

        except FileNotFoundError:
            continue

# Print out a dictionary of all files more than 100 MB (104857600 bytes) and their file sizes in bytes.
print(file_100mb_and_above)

# if you choose to delete all the files found, you can use a for loop and
# the keys of the file_100mb_and_above dictionary to delete them
# Use os.unlink(path) to permanently delete the files or use send2trash to send them to the recycle bin.
