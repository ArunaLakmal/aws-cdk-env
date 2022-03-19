from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_eks as eks,
    aws_ec2 as ec2
)
from constructs import Construct

class TcCdkEksStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.IVpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        cluster = eks.Cluster(self, "TCCDKEKS",
            version=eks.KubernetesVersion.V1_21,
            default_capacity=3,
            vpc=vpc,
            default_capacity_instance=ec2.InstanceType("t3.medium")
        )