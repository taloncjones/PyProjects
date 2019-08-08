# File: GetStockPrice.py
# Use: Looks up stock tickers (given by user) and returns info from finance.yahoo.com
# Author: Talon Jones

# Purpose: Learn webscraping via BS4, logging

import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='GetStockPrice.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def isFloat(string):
    # Attempts to convert string to float. Returns True if successful, otherwise False
    try:
        float(string)
        return True
    except ValueError:
        return False


def getYesNo(question):
    # Gets user input in y/yes/n/no form and returns True or False.
    y_n = ''
    while True:
        y_n = input(question).lower()
        if y_n in {'y', 'yes'}:
            return True
        elif y_n in {'n', 'no'}:
            return False
        else:
            print('Invalid option. Please enter y/n.')


def isTicker(search):
    # Check if the string given is a ticker symbol. If not, ask user to clarify
    url = 'https://query2.finance.yahoo.com/v1/finance/search?quotesCount=1&newsCount=0&q=%s' % (search)
    logging.info(url)
    r = requests.get(url)
    quote = r.json()['quotes']
    if len(quote) == 0:
        return (-1.0, search)
    if search.upper() != quote[0]['symbol']:
        y_n = getYesNo('Did you mean %s - %s?' % (quote[0]['symbol'], quote[0]['shortname']))
        if y_n:
            search = quote[0]['symbol']
        elif not y_n:
            return (-1.0, search)
    return (getStockPrice(search), search)


def getStockPrice(ticker):
    # Look up current ticker price and return float containing price or -1 if error
    url = 'https://finance.yahoo.com/quote/%s?p=%s' % (ticker, ticker)
    logging.info(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'xml')
    try:
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',
                                                                                                                  '')
    except:
        return -1.0
    return float(price) if isFloat(price) else -1.0


if __name__ == '__main__':
    while True:
        searches = input("Please enter stock ticker (Separate multiple tickers with ',': ")
        for search in searches.split(','):
            search = search.strip().upper()
            if search == 'EXIT':
                exit(1)
            else:
                price, ticker = isTicker(search)
                if price >= 0:
                    print(ticker, price)
                else:
                    print('%s not found.' % search)
