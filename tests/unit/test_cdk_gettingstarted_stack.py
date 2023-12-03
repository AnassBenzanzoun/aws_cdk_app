import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_gettingstarted.cdk_gettingstarted_stack import CdkGettingstartedStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_gettingstarted/cdk_gettingstarted_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkGettingstartedStack(app, "cdk-gettingstarted")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
