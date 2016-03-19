# This file mainly for debugging during dev. Gives an idea of what the data being returned looks like
# without having to put stuff into the database.

import json


def displayCategories(api_response):
        j = json.loads(api_response.encode('ascii','ignore').decode())
        i = 0
        results = j['results']

        while i < len(results):
            category = results[i]

            print('Category #: ', str(i))
            print('Name: ', category['name'])
            print('Sort Name: ', category['sort_name'])
            print('Category id: ', category['id'])
            print('Category short name: ', category['shortname'])

            i+=1