from flask import Flask, request, jsonify, send_from_directory
import os
from datetime import datetime
import base64
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '').strip()
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '').strip()
AWS_REGION = os.getenv('AWS_REGION', '').strip()
S3_BUCKET = os.getenv('S3_BUCKET', '').strip()

print(f"AWS_REGION: {AWS_REGION}")
print(f"S3_BUCKET: {S3_BUCKET}")
print(f"AWS_ACCESS_KEY_ID: {'*' * len(AWS_ACCESS_KEY_ID) if AWS_ACCESS_KEY_ID else 'NOT SET'}")
print(f"AWS_SECRET_ACCESS_KEY: {'*' * len(AWS_SECRET_ACCESS_KEY) if AWS_SECRET_ACCESS_KEY else 'NOT SET'}\n")

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('public', filename)

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    image = data.get('image')
    if not image or not image.startswith('data:image'):
        return jsonify({'success': False, 'message': 'Invalid image data.'}), 400

    try:
        # Decode base64 image
        header, encoded = image.split(',', 1)
        image_data = base64.b64decode(encoded)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        filename = f'capture_{timestamp}.png'
        
        # Upload to S3
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=f'pic/{filename}',
            Body=image_data,
            ContentType='image/png'
        )
        
        return jsonify({'success': True, 'message': f'Photo uploaded to S3: pic/{filename}'})
    
    except Exception as e:
        error_msg = str(e)
        print(f"[ERROR] Upload failed: {error_msg}")
        return jsonify({'success': False, 'message': f'Upload failed: {error_msg}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
