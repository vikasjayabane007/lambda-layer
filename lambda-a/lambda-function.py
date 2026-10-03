from common.utils import clean_name


def lambda_handler(event, context):

    name = event.get("name", "vikas")

    cleaned_name = clean_name(name)

    return {
        "statusCode": 200,
        "message": f"Hello {cleaned_name}"
    }