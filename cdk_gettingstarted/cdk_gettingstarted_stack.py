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

        # Create IAM Policy for Lambda function
        lambda_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["lambda:InvokeFunction"],
            resources=["*"],  # You can refine this to a specific resource
        )

        # Create Lambda function with the IAM policy
        my_lambda = lambda_.Function(
            self,
            "CdkGettingstartedLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="handler.lambda_handler",
            code=lambda_.Code.from_asset("./cdk_gettingstarted/lambda_functions"),
            initial_policy=[lambda_policy],  # Assign the policy directly
        )

        # Create API Gateway
        api = apigw.RestApi(
            self,
            "api",
            rest_api_name="api service",
            description="api interface for our lambda function",
            deploy_options={"stage_name": "prod"},
        )

        get_widgets_integration = apigw.LambdaIntegration(my_lambda)

        api.root.add_method("GET", get_widgets_integration)  # GET /
