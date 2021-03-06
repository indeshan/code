#HOW TO USE: python3 siteMapCheck.py https://www.shopclues.com/sitemap.xml

import sys
from xml.etree import ElementTree

import requests


def main(args):
    if len(args):
        result = requests.request('GET', args[0])
        if result.status_code == 200:
            sitemap_xml = ElementTree.fromstring(result.text)

            urls = []
            for loc in sitemap_xml:
                urls.append(loc[0].text)

            print("Found: {} urls".format(len(urls)))

            for url in urls:
                result = requests.request('GET', url)
                print(result.status_code, url)


if __name__ == "__main__":
    main(sys.argv[1:])
