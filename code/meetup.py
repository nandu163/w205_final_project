# Primary control over data reading / writing to DB

from dynamodb.connectionManager import ConnectionManager
from meetup_data.meetupApiSetup import MeetupSetup
from meetup_data.categories import Categories


# get connection to DynamoDB instance
conn = ConnectionManager()
ms = MeetupSetup()

# instantiate the Categories class, pass in base url and key for API access
category_url = ms.url_path + ms.category_path
categories = Categories(category_url, ms.key)

# get the categories from the API
category_response = categories.get_categories()

# insert the categories into the DB from the API
categories.insert(category_response, conn.db)

# retrieve a category from the DB
categories.retrieve_category(1, conn.db)
