#! python 3
# stopwatch.py - A simple stopwatch program with a count up timer.

import time
import datetime
import threading

# Count up timer
def timer_display():
    """Displays time in hh:mm:ss format"""

    secs = 0
    while True:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=secs)
        print(timer, end='\r')

        # Delays the program one second
        time.sleep(1)

        secs += 1


# Stopwatch function
def stopwatch():
    """Displays laps when user presses enter"""

    start_time = time.time()  # Get the lap's start time
    last_time = start_time
    lap_num = 1

    try:
        while True:
            input()

            lap_time = round(time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)
            print('\nLap #%s: %s (%s)\n' % (lap_num, total_time, lap_time), end='')
            lap_num += 1
            last_time = time.time()     # Reset the last lap time
    except EOFError:
        print('\n')


try:
    # Display the program's instruction
    print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl + C to quit.')
    input()  # Press Enter to begin.
    print('Started')

    # Create a thread for the stopwatch function to allow both functions work at the same time
    thread_obj = threading.Thread(target=stopwatch)
    thread_obj.start()
    timer_display()
except KeyboardInterrupt:
    # Handle the Ctrl + C exception to keep its error message from displaying
    print('Done')
