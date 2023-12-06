from aws_cdk import Stack, aws_dynamodb as dynamodb
from constructs import Construct


class DynamoDBStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = dynamodb.TableV2(
            self,
            "Table",
            partition_key=dynamodb.Attribute(
                name="pk", type=dynamodb.AttributeType.STRING
            ),
            contributor_insights=True,
            table_class=dynamodb.TableClass.STANDARD_INFREQUENT_ACCESS,
            point_in_time_recovery=True,
        )

        # Export the table name and ARN
        # CfnOutput(self, "MyTableArn", value=my_table.table_arn)
        # CfnOutput(self, "MyTableName", value=my_table.table_name)
