import os
import gdax
import re
import requests

def ethereumprice():
    public_client = gdax.PublicClient()
    data = public_client.get_product_ticker(product_id='ETH-EUR')

    return data["price"]

def bitcoinprice(event, context):
    public_client = gdax.PublicClient()
    data = public_client.get_product_ticker(product_id='BTC-EUR')

    return data["price"]

def apidata(uri):
    data = requests.get(uri)
    json_data = data.json()
    return json_data

def ethereumbalance():
    dane = apidata("https://api.ethplorer.io/getAddressInfo/0x2debdde3357c888ce12005d39e3c969efd1acbff?apiKey=freekey")
    return dane["ETH"]["balance"]

def bitcoinbalance():
    dane = apidata("https://blockexplorer.com/api/addr/18KqdrNe9X8FVmo7s2vNmNp5C4p5oAgSkx")
    return dane["balance"]

def eurotopln():
    pln = apidata("https://api.fixer.io/latest?symbols=EUR,PLN")
    return pln["rates"]["PLN"]

def ethereumtopln(ethbalance, ethprice, pln):
    return float(ethbalance) * float(ethprice) * float(pln)

def bitcointopln(bitcoinbalance, btcprice, pln):
    return float(bitcoinbalance) * float(btcprice) * float(pln)

def sumprofit(ethpln, btcpln):
    return float(ethpln) + float(btcpln)


def szalas(event, context):
    ethprice = ethereumprice()
    btcprice = bitcoinprice(event, context)
    ethbalance = ethereumbalance()
    europln = eurotopln()
    ethpln = ethereumtopln(ethbalance, ethprice, europln)
    btcbalance = bitcoinbalance()
    btcpln = bitcointopln(btcbalance, btcprice, europln)
    suma = sumprofit(ethpln, btcpln)

    html_template = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/')

    with open(os.path.join(html_template, 'index.html'), 'r') as template:
        html = template.read()
        # html_price = re.sub(r'<% ethprice %>', ethprice, html)
        # html_price = re.sub(r'<% btcprice %>', btcprice, html_price)
        html_price = re.sub(r'<% ethbalance %>', str(ethbalance), html)
        html_price = re.sub(r'<% ethpln %>', str(ethpln), html_price)
        html_price = re.sub(r'<% btcbalance %>', str(btcbalance), html_price)
        html_price = re.sub(r'<% btcpln %>', str(btcpln), html_price)
        html_price = re.sub(r'<% suma %>', str(suma), html_price)


    response = {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/html',
        },
        "body": html_price
    }

    return response