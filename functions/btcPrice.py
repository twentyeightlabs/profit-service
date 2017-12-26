import gdax

def checkbtcprice(event, context):

    public_client = gdax.PublicClient()
    data = public_client.get_product_ticker(product_id='BTC-EUR')
    btcprice = data["price"]

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'text/html',
        },
        "body": btcprice
    }

    return response