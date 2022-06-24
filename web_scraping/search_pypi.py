#! python3
# search_pypi.py - Searches pypi and opens the results of the searched term on the first page.

import requests
import webbrowser
import bs4
import sys  # For alternative 2

# PROMPTING USER TO ENTER SEARCH TERM OF PRODUCT THEY WANT
try:
    print('Search PYPI'.center(40, '*'))
    search_term = input('Search for: ')
    print('Searching...')   # Display text while downloading the search result page
    res = requests.get('https://pypi.org/search/?q=' + search_term)
    res.raise_for_status()

    # Retrieve top search result links
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Open a browser tab for each result
    link_elements = soup.select('.package-snippet')

    # If len(link_elements) is less than 5, it would be chosen which means less than 5 links was found.
    num_open = min(5, len(link_elements))

    for i in range(num_open):
        url_open = 'https://pypi.org' + link_elements[i].get('href')
        print('Opening', url_open)
        webbrowser.open(url_open)
    
    # Tell the user when nothing is found
    if len(link_elements) == 0:
        print('No result')

except Exception as exc:
    print('There is a problem: %s' % exc)


# ALTERNATIVE 2
# GETTING USER INPUT FROM COMMAND LINE ARGUMENT
# Run from the terminal or run dialog. A .bat file linking to this file has to be created
"""
Create a .bat linking to the path of this file.

if batch file name is search_pypi.bat; on the terminal or run dialogue, enter: search_pypi pyperclip 
to search for pyperclip.
"""

"""
try:
    print('Searching...')   # Display text while downloading the search result page
    res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()

    # Retrieve top search result links
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Open a browser tab for each result
    link_elements = soup.select('.package-snippet')

    # If len(link_elements) is less than 5, it would be chosen which means less than 5 links was found.
    num_open = min(5, len(link_elements))

    for i in range(num_open):
        url_open = 'https://pypi.org' + link_elements[i].get('href')
        print('Opening', url_open)
        webbrowser.open(url_open)

    # Tell the user when nothing is found
    if len(link_elements) == 0:
        print('No result')

except Exception as exc:
    print('There is a problem: %s' % exc)
"""
