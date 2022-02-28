#!/usr/bin/env python3
"""
Downloads and extracts a text version of the UCI thesis manual.
"""
import re
import os
import requests
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup as Soup

class Section(object):
    def __init__(self, num, title, url):
        self.num = num
        self.fname = f'{num:02}-{url.split("/")[-1]}.md'
        self.title = title
        self.url = url

def scrape_thesis_manual(dir_name, url):
    # get the whole webpage and parse the html
    html = requests.get(url, verify=False).content
    doc = Soup(html, 'html.parser')

    # array with all the "<ul></ul>" elements
    all_lists = doc.find("body").find_all('ul')
    
    # upon inspecting the output of this for loop:
    # for i in all_lists:
    #     print(f'all_lists[{i}]: {i}\n\n')
    # exit(0)

    # it seems that all_lists[5] is the list with
    # the urls of all the sections of the manual.
    # if that is no longer the case, change the
    # '5' below.
    html_toc = all_lists[5]
    
    # select all elements <a></a> in our toc
    html_toc = html_toc.select('li a')
    toc = []
    for a in html_toc:
        # get the pretty name and the link of this <a> tag
        href = a.attrs.get('href', None).strip()
        title = a.text.strip()
        # if the <a> tag has the attribute 'href', and
        # its value starts with 'https://' (and not
        # something weird like a javascript thingy),
        # then save it in array toc
        if href and f'https://' == href[:8]:
            # print(f'link: {href}')
            toc.append((title,href))

    # ok, so now we have the array toc with all the urls.
    # let's now construct the chapters by scraping one
    # section at the time
    prev_sec = None
    this_sec = None
    next_sec = None
    for i,(title,url) in zip(range(1,len(toc)+1),toc):
        # pack the info for the "next section"
        prev_sec = this_sec
        this_sec = next_sec
        next_sec = Section(i, title, url)

        # skip the first loop, to move "next_this" to "this_sec"
        if i == 1:
            continue
        
        # now, let's get "this" section in a file
        scrape_section(dir_name, prev_sec, this_sec, next_sec)

    # makes the last section
    scrape_section(dir_name, this_sec, next_sec, None)
        
def scrape_section(dir_name, prev_sec, this_sec, next_sec):
    print(f'Fetching "{this_sec.title}"');

    # get the html
    html = requests.get(this_sec.url, verify=False).content
    doc = Soup(html, 'html.parser')
    
    # get the <div> with all the section
    content = doc.find(id='s-lg-guide-main')

    # get list of titles and text of the section
    subsections = content.find_all(class_='s-lib-box-container')

    # write file
    with open(os.path.join(dir_name, this_sec.fname), 'w') as sec_file:
        # Main header of the section
        sec_file.write(f'# {this_sec.num}. {this_sec.title}\n')
        sec_file.write(f'| [source]({this_sec.url})')

        # Navigation Buttons to previous and next sections
        if prev_sec or next_sec:
            if prev_sec:
                sec_file.write(
                    f' | [{prev_sec.num}. {prev_sec.title}]({prev_sec.fname})')
            if next_sec:
                sec_file.write(
                    f' | [{next_sec.num}. {next_sec.title}]({next_sec.fname})')
            sec_file.write(' |\n\n')
            
        # Content of this section
        for s in subsections:
            # find and write subtitle
            subtitle = s.find('h2')
            if subtitle:
                subtitle = subtitle.text.strip()
                sec_file.write(f'## {subtitle}\n\n')

            # find and write content of subsection
            subcontent = s.find(class_='clearfix')
            if subcontent:
                subcontent = subcontent.text
                # remove weird similar to underscore character found
                subcontent = re.sub(r' ', '', subcontent)
                # make equal paragraph skips
                subcontent = re.sub(r'\n+', '\n\n', subcontent)
                # replace marks found in the text that bother Markdown
                subcontent = re.sub(r'\*\*\*', '(!)', subcontent).strip()
                sec_file.write(f'{subcontent}\n\n')
    
if __name__ == '__main__':
    subdir = 'manual'
    root_url = 'http://guides.lib.uci.edu/gradmanual/'
    
    # change working directory to script's path
    oldpath = os.getcwd()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # create subfolder
    try:
        os.mkdir(subdir)
    except:
        pass
    
    # obtain the manual
    scrape_thesis_manual(subdir, root_url)

    # restore the old current directory
    os.chdir(oldpath)
