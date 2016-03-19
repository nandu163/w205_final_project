"""
Categories class
Gets the category list from the Meetup API
Inserts, Updates, Deletes categories
"""

from .display import displayCategories
import json
import requests
import boto3


class Categories:

    def __init__(self, path, key):

        self.path = path
        self.key = key


    def get_categories(self):

        params = {'key': self.key}
        result = requests.get(self.path, params)
        response = result.text
        return response

        # just for debugging
        # displayCategories(response)

    def insert(self, categories, dynamodb):

        cats = json.loads(categories.encode('ascii', 'ignore').decode())
        counter = 0
        results = cats['results']
        category_table = dynamodb.Table('Category')

        while counter < len(results):

            cat = results[counter]

            category_table.put_item(
                Item={
                    'category_id': cat['id'],
                    'name': cat['name'],
                    'short_name': cat['shortname'],
                    'sort_name': cat['sort_name']
                }
            )

            counter += 1

    def retrieve_category(self, cat_id, dynamodb):

        category_table = dynamodb.Table('Category')
        category = category_table.get_item(
            Key={
                'category_id': cat_id,
                'name': 'Arts & Culture'
            }
        )

        item = category['Item']
        print(item)