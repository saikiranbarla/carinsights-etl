import json
import boto3
import psycopg2
import csv
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # 1. Reading S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processing file from bucket: {bucket}, key: {key}")

    # 2. Download file to /tmp
    local_path = f"/tmp/{key.split('/')[-1]}"
    s3.download_file(bucket, key, local_path)

    # 3. Connect to RDS PostgreSQL
    conn = psycopg2.connect(
        host=os.environ['RDS_HOST'],
        user=os.environ['RDS_USER'],
        password=os.environ['RDS_PASSWORD'],
        dbname=os.environ['RDS_DB']
    )
    cursor = conn.cursor()

    # 4. Read CSV and insert into PostgreSQL
    with open(local_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                """
                INSERT INTO sales_table (order_id, customer_name, product, quantity, price, order_date)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (row['order_id'], row['customer_name'], row['product'], 
                 row['quantity'], row['price'], row['order_date'])
            )

    conn.commit()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps("ETL Completed Successfully")
    }
