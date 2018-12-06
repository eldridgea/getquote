#!/usr/bin/python
"""Stock Data provided for free by IEX. View IEX's Terms of Use: https://iextrading.com/api-exhibit-a/."""
import requests
import json
from sys import argv

def getquote(ticker):
    ticker = ticker.upper()
    response = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols=' + ticker + '&types=quote&range=1m')
    return response.json()[ticker]["quote"]["latestPrice"]

def main():
    print getquote(str(argv[1]))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()