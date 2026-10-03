from common.utils import calculate_total


def lambda_handler(event, context):

    price = event.get("price", 10)
    quantity = event.get("quantity", 5)

    total = calculate_total(price, quantity)

    return {
        "statusCode": 200,
        "total": total
    }