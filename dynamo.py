#!/Users/michelnossin/anaconda/bin/python

#We will use $HOME/.aws/credentials and config set by aws cli. (and not boto.client())
#python -m pip install boto3
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='flight_events',
    KeySchema=[
        {
            'AttributeName': 'flight',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'day',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'flight',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'day',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='flight_events')

# Print out some data about the table.
print(table.item_count)
