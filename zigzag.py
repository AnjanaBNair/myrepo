# zigzag.py - Zigzag animation.

import time
import sys

indent = 0  # How many spaces to indent.
indentIncreasing = True   # Whether the indent is increasing or not.

try:
    while True:  # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(2)  # pause for 1/10 of a second.
        if indentIncreasing:
            #  increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction
                indentIncreasing = False
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
    
