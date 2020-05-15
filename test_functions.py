import datetime

import boto3
import freezegun

from functions import create_file, five_days_from_now


def test_five_days_from_now():
    # Freezing time
    with freezegun.freeze_time("2012-01-14"):
        assert five_days_from_now() == datetime.datetime.now()

    # call five_days_from_now without freeze
    assert five_days_from_now() != datetime.datetime.now()


def test_create_file(s3_client):
    # Create test.txt file
    create_file("tests/test.txt", "hello world")

    # get the object contents
    object = s3_client.get_object(Bucket="bucket.proxyroot.com", Key="tests/test.txt")
    data = object["Body"].read().decode("utf-8")

    assert data == "hello world"
