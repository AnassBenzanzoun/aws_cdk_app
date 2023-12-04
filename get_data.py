import boto3
import json

session = boto3.session.Session(region_name='us-east-1')
pricing = session.client('pricing')

service_codes = ['AmazonEC2', 'AmazonS3', 'AmazonRDS']  # Replace with actual service codes

services = []
for service_code in service_codes:
    response = pricing.get_products(
        ServiceCode=service_code,
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'location',
                'Value': 'US East (N. Virginia)'
            },
        ],
        MaxResults=100
    )

    for product in response['PriceList']:
        product_obj = json.loads(product)
        if 'productFamily' in product_obj['product']:
            product_attributes = product_obj['product']['productFamily']
            services.append(product_attributes)

# Write the data to a file
with open('services.json', 'w') as f:
    json.dump(services, f)