import requests
from bs4 import BeautifulSoup

def stockPrize(stockcode):
    stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stockcode)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")

    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item)+1
            latestPrice=data_array[index].split('"')[1]
            return latestPrice


print(stockPrize("ZYDUSLIFE"))