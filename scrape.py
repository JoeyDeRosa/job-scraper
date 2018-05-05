'''This script runs in Python 3'''
from bs4 import BeautifulSoup
import requests
import os
import datetime

now = datetime.datetime.now()

'''Put the full url of the site you want to search here as a string '''

site_url = 'https://www.bing.com/search?q=youtube&qs=n&form=QBLH&sp=-1&ghc=2&pq=youtube&sc=9-7&sk=&cvid=3B92335F96D9428783BA79DA1A72D771'

'''Put the key words you want to search for here as strings'''

key_words = ['blog']

def make_search(site_url):
    search_request = requests.get(site_url, auth=('user', 'pass'))
    soup = BeautifulSoup(search_request.text, 'html.parser')
    return soup

def scrape_links(key_words):
    links = []
    site_soup = make_search(site_url)
    for link in site_soup.find_all('a'):
        for word in key_words:
            if word in str(link.get('href')):
                links.append(str(link.get('href')))
    return links

def create_link_file():
    links = scrape_links(key_words)
    file = open('./links_scraped/' + str(now)[0:10] + '_links.txt', 'w')
    for link in links:
        file.write(link + '\n')
    file.close()

if __name__ == '__main__':
    create_link_file()