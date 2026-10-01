from requests import get
from datetime import date, timedelta
from twilio.rest import Client

YESTERDAY = str(date.today() - timedelta(days=1))
DAY_BEFORE_YESTERDAY = str(date.today() - timedelta(days=2))
STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
VANTAGE_API = 'LJG9O39B4NPS1PRA'
VANTAGE_ENDPOINT = 'https://www.alphavantage.co/query?'
vantage_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': VANTAGE_API
}
NEWS_API = 'c98c5c039a0045bebe51bc5dc444aaab'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything?'
news_params = {
    'q': 'Tesla',
    'apikey': NEWS_API
}

sid = ''
auth_token = ''
client_secret = ''
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# vantage_response = get(VANTAGE_ENDPOINT, params=vantage_params)
# vantage_response.raise_for_status()
# vantage_data = vantage_response.json()
#
# CAN ALSO ADD DATA TO A LIST AND USE INDEX KEYS INSTEAD OF KEYWORD
# dby_price = float(vantage_data['Time Series (Daily)'][DAY_BEFORE_YESTERDAY]['4. close'])
# y_price = float(vantage_data['Time Series (Daily)'][YESTERDAY]['4. close'])
# price_change = abs(((y_price - dby_price) * 100) / dby_price)

# if price_change >= 5:
news_response = get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
articles = news_data = news_response.json()['articles']
three_articles = articles[:3]
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

client = Client(sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+17372324091',
        to='+12709963838'
    )
