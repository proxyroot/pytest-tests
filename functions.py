import datetime

import boto3


def five_days_from_now():
    return datetime.datetime.now()


def create_file(path, content):
    """
    Creates a file in s3 bucket given a path to the file and content to write
    :path: <str>
    :content: <str>
    """
    client = boto3.client("s3", region_name="us-east-1")
    client.put_object(
        Body=content.encode("utf-8"), Bucket="bucket.proxyroot.com", Key=path
    )
