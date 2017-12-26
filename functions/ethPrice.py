import gdax

def checkethprice(event, context):

    public_client = gdax.PublicClient()
    data = public_client.get_product_ticker(product_id='ETH-EUR')
    ethprice = data["price"]

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'text/html',
        },
        "body": ethprice
    }

    return response
