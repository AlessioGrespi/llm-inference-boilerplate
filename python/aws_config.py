import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

# Load environment variables from the .env file
load_dotenv()

# Retrieve AWS credentials and region from the .env file
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Initialize the Bedrock client
bedrock_client = boto3.client(
    "bedrock-runtime",
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)
