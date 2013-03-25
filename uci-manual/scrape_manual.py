#!/usr/bin/env python2
"""
Downloads and extracts a text version of the UCI thesis manual.
"""

from bs4 import BeautifulSoup as Soup
import urllib2

def get_contents(url, output_name):
    html = urllib2.urlopen(url).read()
    manual_content = Soup(html).findAll('div', {'class': 'sca2Column'})[0]
    with open(output_name + '.txt', 'w') as fh:
        fh.write(manual_content.text.encode('utf8'))

get_contents('http://special.lib.uci.edu/dissertations/electronic/tdmanuale.html', 'toc')
for section in range(1,8):
    url = 'http://special.lib.uci.edu/dissertations/electronic/td%de.html' % section
    get_contents(url, 'section%d' % section)
