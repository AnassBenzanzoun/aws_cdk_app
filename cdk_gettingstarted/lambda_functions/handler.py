import boto3
import json

# Create a DynamoDB resource
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    try:
        # Define the DynamoDB table
        table_name = "YourDynamoDBTableName"  # Replace with your table name
        table = dynamodb.Table(table_name)

        # Scan the DynamoDB table to retrieve all items
        response = table.scan()

        # Extract the items from the response
        items = response["Items"]

        # Prepare the response containing the items as JSON
        json_response = {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(items),
        }

        return json_response

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Exception: {e}")

        # Return a meaningful error response
        error_response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"}),
        }
        return error_response
