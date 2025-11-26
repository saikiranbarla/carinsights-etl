import os
import boto3
from datetime import datetime

RAW_BUCKET = os.environ.get("S3_RAW_BUCKET")

def upload_directory_to_s3(local_folder, bucket):
    s3 = boto3.client("s3")

    for root, dirs, files in os.walk(local_folder):
        for file in files:
            if file.endswith(".csv"):
                full_path = os.path.join(root, file)
                s3_key = full_path.replace("\\", "/")

                print(f"Uploading: {full_path} -> s3://{bucket}/{s3_key}")
                s3.upload_file(full_path, bucket, s3_key)

if __name__ == "__main__":
    print("Starting ETL upload job...")

    folder = "sample_data"
    if not os.path.exists(folder):
        print("sample_data folder does not exist. Exiting.")
        exit(1)

    upload_directory_to_s3(folder, RAW_BUCKET)

    print("ETL upload completed successfully at:", datetime.now())
