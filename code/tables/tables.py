import boto3


class Tables:

    def create_category_tbl(self, dynamodb):

            categoryTable = dynamodb.create_table(
               AttributeDefinitions=[

                {
                  'AttributeName': 'category_id',
                  'AttributeType': 'N'
                },
                {
                  'AttributeName': 'name',
                  'AttributeType': 'S'
                },
              ],
              TableName='Category',
              KeySchema=[

                {
                  'AttributeName': 'category_id',
                  'KeyType': 'HASH'

                },
                {
                  'AttributeName': 'name',
                  'KeyType': 'RANGE'
                },
              ],

              ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10

              }
            )

            print("Table Status: ", categoryTable.table_status)
            print(list(dynamodb.tables.all()))


    def delete_category_tbl(self, dynamodb):

        categoryTable = dynamodb.Table('Category')
        categoryTable.delete()
        print(list(dynamodb.tables.all()))

