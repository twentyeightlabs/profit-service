import json
import requests
import re
import urllib


def profit(event, context):
    uri = "https://api.coinbase.com/v2/prices/btc-usd/spot"
    data = requests.get(uri)
    json_data = data.text
    dane = json.loads(json_data)
    price = dane["data"]["amount"]

    html = '''
    <div> Current BTC price on GDAX is: <% price %> <div>'''
    html_price = re.sub(r'<% price %>', price, html)


    response = {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/html',
        },
        "body": html_price
    }

    return response