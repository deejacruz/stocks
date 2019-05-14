from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import schedule
import time 

def job():
    quote_page = ['https://www.fool.com/quote/nasdaq/facebook/fb/', 
        'https://www.fool.com/quote/nasdaq/tesla-motors/tsla/', 
        'https://www.fool.com/quote/nasdaq/apple/aapl/', 
        'https://www.fool.com/quote/nasdaq/netflix/nflx', 
        'https://www.fool.com/quote/nasdaq/alphabet-a-shares/googl', 
        'https://www.fool.com/quote/nasdaq/alphabet-c-shares/goog', 
        'https://www.fool.com/quote/nasdaq/amazon/amzn', 
        'https://www.fool.com/quote/nasdaq/lyft/lyft/', 
        'https://www.fool.com/quote/nasdaq/zoom-video-communications/zm/', 
        'https://www.fool.com/quote/nasdaq/roku/roku', 
        'https://www.fool.com/quote/nyse/walt-disney/dis', 
        'https://www.fool.com/quote/nyse/general-electric/ge', 
        'https://www.fool.com/quote/nyse/walmart-inc/wmt', 
        'https://www.fool.com/quote/nyse/berkshire-hathaway-a-shares/brk-a/', 
        'https://www.fool.com/quote/nyse/berkshire-hathaway-b-shares/brk-b/', 
        ]
    data = []
    for pg in quote_page:
        page = urlopen(pg)
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('h2', attrs={'class': 'company-name'})
        name = name_box.text.strip()
        price_box = soup.find('span', attrs={'class': 'current-price'})
        price = price_box.text.strip()
        data.append((name, price))
    with open('stocks.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for name, price in data: 
            writer.writerow([name, price, datetime.now()])
schedule.every().monday.at("16:30").do(job)
schedule.every().tuesday.at("16:30").do(job)
schedule.every().wednesday.at("16:30").do(job)
schedule.every().thursday.at("16:30").do(job)
schedule.every().friday.at("16:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)