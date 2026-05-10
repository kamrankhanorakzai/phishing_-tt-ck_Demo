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

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def delete_pics_from_s3():
    """Delete all pictures from the 'pic/' folder in S3"""
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

        # Collect all object keys to delete
        objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]

        # Delete all objects in batches (S3 allows up to 1000 objects per delete request)
        batch_size = 1000
        for i in range(0, len(objects_to_delete), batch_size):
            batch = objects_to_delete[i:i + batch_size]
            delete_response = s3_client.delete_objects(
                Bucket=S3_BUCKET,
                Delete={'Objects': batch}
            )

            deleted_count = len(delete_response.get('Deleted', []))
            print(f"Deleted {deleted_count} file(s) from S3")

            # Print any errors
            if 'Errors' in delete_response:
                for error in delete_response['Errors']:
                    print(f"Error deleting {error['Key']}: {error['Message']}")

        print(f"\n✓ All pictures deleted from S3 'pic/' folder!")

    except Exception as e:
        print(f"✗ Error deleting pictures: {str(e)}")

if __name__ == '__main__':
    # Ask for confirmation before deleting
    confirm = input("⚠️  This will delete ALL pictures from S3 'pic/' folder. Are you sure? (yes/no): ")
    if confirm.lower() == 'yes':
        delete_pics_from_s3()
    else:
        print("Operation cancelled.")
