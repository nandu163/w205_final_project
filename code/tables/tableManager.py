# Primary control over the application

from connectionManager import ConnectionManager
from tables import Tables


# get connection to DynamoDB instance
conn = ConnectionManager()
tables = Tables()

tables.create_category_tbl(conn.db)

# delete table code:
#tables.delete_category_tbl(conn.db)
