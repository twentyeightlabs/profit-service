import gdax
import requests

def bitcoinprice():
    public_client = gdax.PublicClient()
    data = public_client.get_product_ticker(product_id='BTC-EUR')

    print(data)

    #return data["price"]

def apidata(uri):
    data = requests.get(uri)
    json_data = data.json()
    return json_data

def ethereumbalance():
    dane = apidata("https://api.ethplorer.io/getAddressInfo/0x2debdde3357c888ce12005d39e3c969efd1acbff?apiKey=freekey")
    return dane["ETH"]["balance"]

# def bitcoinbalance():
#     dane = apidata("https://blockexplorer.com/api/addr/18KqdrNe9X8FVmo7s2vNmNp5C4p5oAgSkx")
#     return dane["balance"]

result = bitcoinprice()
#print(result)
#print(ethereumbalance())
# print(bitcoinbalance())