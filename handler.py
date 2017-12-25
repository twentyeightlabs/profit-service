import json
import requests
import re
import os
import gdax


def profit(event, context):

    public_client = gdax.PublicClient()
    data = public_client.get_product_ticker(product_id='ETH-EUR')
    ethprice = data["price"]

    # uri = "https://api.coinbase.com/v2/prices/btc-usd/spot"
    # data = requests.get(uri)
    # json_data = data.text
    # dane = json.loads(json_data)
    # ethprice = dane["data"]["amount"]

    html_template = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/')

    with open(os.path.join(html_template, 'index.html'), 'r') as template:
        html = template.read()
        html_price = re.sub(r'<% ethprice %>', ethprice, html)

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'text/html',
        },
        "body": html_price
    }

    return response