'''This script runs in Python 3'''
from bs4 import BeautifulSoup
import requests
import os
import datetime
import csv

now = datetime.datetime.now()

'''Put the full url of the site you want to search here as a string '''

site_url = 'https://www.tacomachamber.org/list/ql/finance-insurance-10'

def make_search(site_url):
    search_request = requests.get(site_url, auth=('user', 'pass'))
    soup = BeautifulSoup(search_request.text, 'html.parser')
    return soup

def scrape_info():
    company_names = []
    company_addresses = []
    company_urls = []
    company_numbers = []
    site_soup = make_search(site_url)
    for company_name in site_soup.findAll('div', {'class': 'mn-title'}):
        company_names.append(company_name.get_text())
    for company_address in site_soup.findAll('div', {'class': 'mn-address'}):
        company_addresses.append(company_address.get_text())
    for company_url in site_soup.findAll('a', {'class': 'mn-print-url'}):
        company_urls.append(str(company_url.get('href')))
    for company_number in site_soup.findAll('li', {'class': 'mn-phone'}):
        company_numbers.append(company_number.get_text())
    while len(company_addresses) < len(company_names):
        company_addresses.append('not found')
    while len(company_urls) < len(company_names):
        company_urls.append('not found')
    while len(company_numbers) < len(company_names):
        company_numbers.append('not found')
    return([company_names, company_addresses, company_urls, company_numbers])

def create_info_file():
    site_info = scrape_info()
    with open ('./info_scraped/' + str(now)[0:10] + '_info.csv', 'w', newline='') as csvfile:
        info_writer = csv.writer(csvfile)
        for i in range(len(site_info[0]) - 1):
            info_writer.writerow([str(site_info[0][i]), str(site_info[1][i]), str(site_info[2][i]), str(site_info[3][i])])

if __name__ == '__main__':
    create_info_file()
