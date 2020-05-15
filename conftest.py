import boto3
import pytest

from moto import mock_s3


@pytest.fixture(scope="function")
def s3_client():
    with mock_s3():
        conn = boto3.resource("s3", region_name="us-east-1")
        # create a bucket
        conn.create_bucket(Bucket="bucket.proxyroot.com")

        client = boto3.client("s3", region_name="us-east-1")

        yield client
