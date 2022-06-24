#! python3
# search_jumia.py - Open the links of the 5 cheapest product for every search term.

import sys              # Used in alternative 2
import webbrowser
import requests
from bs4 import BeautifulSoup

# PROMPTING USER TO ENTER SEARCH TERM OF PRODUCT THEY WANT
try:
    # Prompt user to enter search term and create a list of each words
    product_name = input('What product are you looking for: ').split(' ')

    # Join the list of words with a '+' in between as it is used in jumia website search
    search = '+'.join(product_name)  # Remove program and save argument (search term to 'search').

    # Download web page of search file
    jumia_res = requests.get('https://www.jumia.com.ng/catalog/?q=' + search)
    jumia_res.raise_for_status()

    # Select (create a list) of class containing price of products from searched term
    jumia_soup = BeautifulSoup(jumia_res.content, 'html.parser')
    result_element = jumia_soup.select('.info > .prc')

    # Prompt the user if the there is no product available for searched term.
    if result_element == []:
        print('No item found for', search)
    
    price_list = []
    for i in range(len(result_element)):

        # Remove item that has no price
        if result_element[i].getText() == '':
            continue

        # Add text of element to a list
        price_list.append(result_element[i].getText())

    # Sort the list in ascending order
    price_list.sort()           # Sort the price list
    sorted_price_list = sorted(price_list, key=len)     # Sorting the list again according to string length
    print(sorted_price_list)

    # <a> elements of all products from search term
    a_elements = jumia_soup.select('.core')

    i = 0  # Counter for opening 5 cheapest products
    while i < 5:
        for j in range(len(a_elements)):
            # Check for the <a> element containing the cheapest prices, get the links and open them in new tabs
            if sorted_price_list[i] in str(a_elements[j]):
                open_url = 'https://www.jumia.com.ng' + a_elements[j].get('href')
                print('Opening', open_url)
                webbrowser.open(open_url)

        i += 1

except Exception as exc:
    print('There is a problem: %s' % exc)


# ALTERNATIVE 2
# GETTING USER INPUT FROM COMMAND LINE ARGUMENT
"""
try:
    # Take search tem from command line argument
    if len(sys.argv) > 1:
        search = '+'.join(sys.argv[1:])  # Remove program and save argument (search term to 'search').

        # Download web page of search file
        jumia_res = requests.get('https://www.jumia.com.ng/catalog/?q=' + search)
        jumia_res.raise_for_status()

        # Select (create a list) of class containing price of products from searched term
        jumia_soup = BeautifulSoup(jumia_res.content, 'html.parser')
        result_element = jumia_soup.select('.info > .prc')

        # Prompt the user if the there is no product available for searched term.
        if result_element == []:
            print('No item found for', search)

        price_list = []
        for i in range(len(result_element)):

            # Remove item that has no price
            if result_element[i].getText() == '':
                continue

            # Add text of element to a list
            price_list.append(result_element[i].getText())

        # Sort the list in ascending order
        price_list.sort()           # Sort the price list
        sorted_price_list = sorted(price_list, key=len)     # Sorting the list again according to string length
        print(sorted_price_list)

        # <a> elements of all products from search term
        a_elements = jumia_soup.select('.core')

        i = 0  # Counter for opening 5 cheapest products
        while i < 5:
            for j in range(len(a_elements)):
                # Check for the <a> element containing the cheapest prices, get the links and open them in new tabs
                if sorted_price_list[i] in str(a_elements[j]):
                    open_url = 'https://www.jumia.com.ng' + a_elements[j].get('href')
                    print('Opening', open_url)
                    webbrowser.open(open_url)

            i += 1

except Exception as exc:
    print('There is a problem: %s' % exc)
"""
