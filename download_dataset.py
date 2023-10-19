import json
import os
import sys
import argparse

from google.cloud import storage
from google.oauth2 import service_account


def scrape_bucket(bucket_name):
    # Instantiate a client
    creds = service_account.Credentials.from_service_account_file(credential_path)
    client = storage.Client(credentials=creds)
    # Retrieve the bucket object
    bucket = client.get_bucket(bucket_name)
    # Download VoxCeleb.zip from the bucket
    blob = bucket.blob("VoxCeleb.zip")
    blob.download_to_filename("VoxCeleb.zip")

    # Unzip VoxCeleb.zip
    os.system("unzip VoxCeleb.zip")
    # Remove VoxCeleb.zip
    os.system("rm VoxCeleb.zip")

    print("Downloaded VoxCeleb dataset to current directory. ")




parser = argparse.ArgumentParser()
parser.add_argument("bucket_name", help="Bucket name", nargs='?', default="audio2face")
parser.add_argument("credential_path", help="Credential path", nargs='?',  default="../remotework-347706-de94e050c66e.json")

args = parser.parse_args()

bucket_name = args.bucket_name
credential_path = args.credential_path


scrape_bucket(bucket_name)
