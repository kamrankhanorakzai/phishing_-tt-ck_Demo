import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
S3_BUCKET = os.getenv('S3_BUCKET')

# Local folder to save images
LOCAL_FOLDER = 'downloaded_pics'
os.makedirs(LOCAL_FOLDER, exist_ok=True)

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def download_pics_from_s3():
    """Download all pictures from the 'pic/' folder in S3"""
    try:
        print(f"Connecting to S3 bucket: {S3_BUCKET}")
        
        # List all objects in the 'pic/' folder
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix='pic/'
        )
        
        if 'Contents' not in response:
            print("No pictures found in S3 'pic/' folder.")
            return
        
        total_files = len(response['Contents'])
        print(f"Found {total_files} file(s) in S3 'pic/' folder.\n")
        
        for idx, obj in enumerate(response['Contents'], 1):
            key = obj['Key']
            filename = os.path.basename(key)
            
            if filename:  # Skip if it's just a folder
                local_path = os.path.join(LOCAL_FOLDER, filename)
                print(f"[{idx}/{total_files}] Downloading: {key}")
                s3_client.download_file(S3_BUCKET, key, local_path)
                print(f"          Saved to: {local_path}\n")
        
        print(f"✓ All pictures downloaded to '{LOCAL_FOLDER}/' folder!")
    
    except Exception as e:
        print(f"✗ Error downloading pictures: {str(e)}")

if __name__ == '__main__':
    download_pics_from_s3()
