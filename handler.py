import json
import requests
import re
import os


def profit(event, context):
    uri = "https://api.coinbase.com/v2/prices/btc-usd/spot"
    data = requests.get(uri)
    json_data = data.text
    dane = json.loads(json_data)
    price = dane["data"]["amount"]

    html_template = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/')

    with open(os.path.join(html_template, 'index.html'), 'r') as template:
        html = template.read()
        html_price = re.sub(r'<% price %>', price, html)

    response = {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/html',
        },
        "body": html_price
    }

    return response