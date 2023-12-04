from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
    aws_iam as iam,
)
from constructs import Construct


class CdkGettingstartedStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function
        my_lambda = lambda_.Function(
            self, "CdkGettingstartedLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="handler.lambda_handler",
            code=lambda_.Code.from_asset('./cdk_gettingstarted/lambda_functions')
        )
        # IAM Policy for Lambda function
        lambda_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["lambda:InvokeFunction"],
            resources=[my_lambda.function_arn]
        )
        my_lambda.add_to_role_policy(lambda_policy)

        # Create API Gateway
        api = apigw.RestApi(self, "widgets-api",
                  rest_api_name="Widget Service",
                  description="This service serves widgets.")

        get_widgets_integration = apigw.LambdaIntegration(my_lambda)

        api.root.add_method("GET", get_widgets_integration)   # GET /
            

        
