#! python3
# rename_dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
import shutil
import os
import re

# Create a regex that matches files with the American date format

date_pattern = re.compile(r"""^(.*?)    # all text before the date
    ((0|1)?\d)-                         # one or two digits for the month
    ((0|1|2|3)?\d)-                     # one or two digits for the day
    ((19|20)?\d{2})                     # four digits for the year
    (.*?)$                              # all text after the date
""", re.VERBOSE)

# Loop through the files in the working directory
for american_date_files in os.listdir('.'):
    print(american_date_files)

    mo = date_pattern.search(str(american_date_files))

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename
    euro_file_name = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute paths.
    abs_working_dir = os.path.abspath('.')
    american_date_files = os.path.join(abs_working_dir, american_date_files)
    euro_file_name = os.path.join(abs_working_dir, euro_file_name)

    # Renaming the files
    print(f'Renaming {american_date_files} to {euro_file_name}')

    # UNCOMMENT the code below before running if you choose to rename the files
    # shutil.move(american_date_files, euro_file_name)


# ALTERNATIVE - Using pathlib module instead of  os module
"""
from pathlib import Path
import shutil
import re

# Create a regex that matches files with the American date format

date_pattern = re.compile(r"""# ^(.*?)    # all text before the date
    # ((0|1)?\d)-                         # one or two digits for the month
    # ((0|1|2|3)?\d)-                     # one or two digits for the day
    # ((19|20)?\d{2})                     # four digits for the year
    # (.*?)$                              # all text after the date
""", re.VERBOSE)

# Loop through the files in the working directory
for american_date_files in Path.cwd().glob('*'):

    mo = date_pattern.search(str(american_date_files))

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename
    euro_file_name = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Renaming the files
    print(f'Renaming {american_date_files} to {euro_file_name}')
    
    # UNCOMMENT the code below before running if you choose to rename the files
    # shutil.move(american_date_files, euro_file_name)
"""
