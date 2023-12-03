from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigatewayv2 as api,
)
from constructs import Construct

class CdkGettingstartedStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function
        my_lambda = lambda_.Function(
            self, "CdkGettingstartedLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="handler.handler",
            code=lambda_.Code.from_asset('./cdk_gettingstarted/lambda_functions')
        )

        # Create API Gateway
        my_api = api.HttpApi(
            self, "CdkGettingstartedApi"
        )

        # Add route with integration
        my_api.add_routes(
            path="/",
            methods=[api.HttpMethod.GET],
            integration=api.HttpIntegration(
                self, "MyHttpIntegration",
                integration_type=api.HttpIntegrationType.AWS_PROXY,
                http_api=my_api
            )
        )
        

        
