import json
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
table_name = "mp2_table" # leaving as is really mp3
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    print(event)

    try:
        intent = event["interpretations"][0]["intent"]

        # Check if 'source' and 'destination' are present in the slots
        if (
            "slots" in intent
            and "source" in intent["slots"]
            and "destination" in intent["slots"]
        ):
            source = intent["slots"]["source"]["value"]["interpretedValue"]
            destination = intent["slots"]["destination"]["value"]["interpretedValue"]

            # Basic input validation
            if not source or not destination:
                raise ValueError("Source and destination must be provided.")

            distance = get_distance_from_dynamodb(source, destination)

            if distance is not None:
                response = close(f"{distance}")
            else:
                response = close(str(-1))
        else:
            response = close(
                "Bad Request: Missing source or destination in the slot values."
            )
    except Exception as e:
        print(f"Error processing Lex intent: {e}")
        response = close(f"An error occurred: {str(e)}")

    return response


def get_distance_from_dynamodb(source, destination):
    try:
        response = table.get_item(Key={"source": source, "destination": destination})
        item = response.get("Item")
        if item:
            return item.get("distance")
        else:
            return None
    except ClientError as e:
        print(f"Error querying DynamoDB: {e}")
        return None


def close(message, fulfillment_state="Fulfilled"):
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": fulfillment_state,
            },
            "intent": {
                "name": "GetDistance",
                "confirmationState": "None",
                "state": fulfillment_state,
            },
        },
        "messages": [{"contentType": "PlainText", "content": message}],
    }
