#! python3
# download_xkcd.py - Downloads every page of XKCD comic.

import requests
import bs4
import os

try:
    url = 'https://xkcd.com'        # starting url
    os.makedirs('xkcd', exist_ok=True)

    while not url.endswith('#'):
        # Download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        # Find the URL of the comic image
        comic_element = soup.select('#comic img')

        # Check if any element was found
        if comic_element == []:
            print('Could not find comic image.')

        # Get the link of the image (from the element found.)
        else:
            comic_url = 'https:' + comic_element[0].get('src')

            # Download the image.
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')

            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

        # Get the Prev button's url.
        prev_link = soup.select('a[rel="prev"]')
        url = 'https://xkcd.com' + prev_link[0].get('href')

    print('Done.')


except Exception as exc:
    print('There is a problem: %s' % exc)
