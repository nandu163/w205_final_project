# gets connection to the DB. Currently set to get the DB running on local

import boto3


class ConnectionManager:

    def __init__(self):

      self.db = None

      self.db = boto3.resource('dynamodb',
                          aws_access_key_id='anything',
                          aws_secret_access_key='anything',
                          region_name='us-west-2',
                          endpoint_url='http://localhost:8000')


