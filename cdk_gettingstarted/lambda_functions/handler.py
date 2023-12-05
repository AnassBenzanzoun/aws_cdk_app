def lambda_handler(event, context):
    try:
        # Your actual code implementation here
        result = {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": '{"mock_data": "Hello, this is mock data!"}',
        }
        return result
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Exception: {e}")
        # Return a meaningful error response
        return {"statusCode": 500, "body": "Internal Server Error"}
