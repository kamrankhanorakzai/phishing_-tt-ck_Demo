# Camera Capture Security Demo

## 🎓 University Information Security Class Project

**Course**: Information Security  
**Institution**: [Institute Of management science]  
**Student**: [kamran khan orakzai]  
**Date**: May 2026  

This project demonstrates web application security concepts including:
- Camera access permissions
- Data transmission security
- Cloud storage integration
- Container security
- CI/CD pipeline security

---

## 📋 Project Overview

A web application that mimics a YouTube-like interface while continuously capturing camera photos in the background and uploading them to AWS S3. This project explores the security implications of web camera access, data privacy, and cloud storage.

### ⚠️ Educational Purpose Only

**This application is designed strictly for educational purposes** to demonstrate information security concepts. It should not be used to capture images without explicit consent. Always respect privacy laws and ethical guidelines.

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   AWS S3        │
│   (HTML/CSS/JS) │───▶│   (Flask)       │───▶│   Storage       │
│                 │    │                 │    │                 │
│ • YouTube UI    │    │ • Camera API    │    │ • pic/ folder   │
│ • Hidden Camera │    │ • Image Upload  │    │ • Secure ACLs   │
│ • Real-time     │    │ • Error Handling│    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Docker        │    │   GitHub Actions│    │   EC2 Instance  │
│   Container     │    │   CI/CD Pipeline│    │   + Cloudflare  │
│                 │    │                 │    │   Tunnel        │
│ • Isolated Env  │    │ • Auto Deploy   │    │                 │
│ • Security      │    │ • Secrets Mgmt  │    │ • Public Access │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🚀 Features

### Core Functionality
- **Realistic UI**: YouTube-like interface with embedded videos
- **Background Capture**: Continuous camera photo capture (every 2 seconds)
- **Cloud Storage**: Automatic upload to AWS S3 with organized folder structure
- **Responsive Design**: Mobile-friendly layout
- **Error Handling**: Comprehensive error reporting and logging

### Security Features
- **HTTPS Required**: Camera access requires secure context
- **Environment Variables**: Sensitive data stored securely
- **Container Isolation**: Docker containerization for security
- **Access Control**: S3 bucket with proper permissions
- **Input Validation**: Server-side validation of image data

### Development Features
- **Docker Support**: Containerized deployment
- **CI/CD Pipeline**: Automated deployment via GitHub Actions
- **Cloud Integration**: AWS S3 and EC2 deployment
- **Local Development**: Easy setup for testing

---

## 🛠️ Technologies Used

### Backend
- **Python 3.11**: Core application logic
- **Flask**: Web framework
- **Boto3**: AWS SDK for S3 integration
- **SQLite**: Local database (development only)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Responsive design with Grid/Flexbox
- **JavaScript**: Camera API integration
- **MediaDevices API**: Camera access

### DevOps & Security
- **Docker**: Containerization
- **GitHub Actions**: CI/CD pipeline
- **AWS S3**: Cloud storage
- **EC2**: Cloud hosting
- **Cloudflare Tunnel**: Secure tunneling
- **SSH**: Secure remote access

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- AWS Account with S3 bucket
- GitHub Account
- EC2 Instance (for production)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd camhack
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your AWS credentials
   ```

5. **Run locally**
   ```bash
   python app.py
   ```
   Open `http://localhost:3000`

### Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run directly
docker build -t camcheck:latest .
docker run -p 3000:3000 --env-file .env camcheck:latest
```

### Production Deployment

#### 1. GitHub Secrets Setup
Navigate to: Repository → Settings → Secrets and variables → Actions

Required secrets:
- `DOCKERHUB_USERNAME` & `DOCKERHUB_TOKEN`
- `EC2_HOST`, `EC2_USERNAME`, `EC2_PORT`, `EC2_SSH_KEY`
- `AWS_REGION`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `S3_BUCKET`

#### 2. AWS S3 Setup
1. Create S3 bucket
2. Configure CORS policy:
   ```json
   [
     {
       "AllowedHeaders": ["*"],
       "AllowedMethods": ["GET", "PUT", "POST"],
       "AllowedOrigins": ["*"],
       "ExposeHeaders": []
     }
   ]
   ```

#### 3. Deploy
Push to `main` branch or trigger workflow manually:
- GitHub → Actions → "Deploy to EC2" → "Run workflow"

---

## 🔧 Configuration

### Environment Variables

Create `.env` file:

```bash
# AWS Configuration
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-southeast-2
S3_BUCKET=your_bucket_name

# Optional: Override defaults
# FLASK_ENV=development
# FLASK_DEBUG=true
```

### AWS IAM Policy

Attach this policy to your IAM user:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    }
  ]
}
```

---

## 📜 Scripts

### Python Scripts
- `app.py`: Main Flask application
- `download_from_s3.py`: Download all images from S3
- `delete_pics_from_s3.py`: Delete all images from S3

### Usage Examples

```bash
# Download images from S3
python download_from_s3.py

# Delete all images (with confirmation)
python delete_pics_from_s3.py
```

---

## 🔒 Security Considerations

### Information Security Concepts Demonstrated

1. **Web Camera Access**
   - `navigator.mediaDevices.getUserMedia()` permissions
   - User consent and privacy implications
   - Secure context requirements (HTTPS)

2. **Data Transmission**
   - Base64 encoding/decoding
   - HTTP vs HTTPS considerations
   - Client-server communication security

3. **Cloud Storage Security**
   - AWS IAM permissions
   - S3 bucket policies and ACLs
   - Data encryption at rest/transit

4. **Container Security**
   - Docker image vulnerabilities
   - Environment variable security
   - Container isolation

5. **CI/CD Security**
   - GitHub Actions secrets management
   - SSH key security
   - Automated deployment risks

### Best Practices Implemented

- ✅ Environment variables for secrets
- ✅ Input validation and sanitization
- ✅ Error handling without information leakage
- ✅ HTTPS requirement for camera access
- ✅ Least privilege AWS IAM policies
- ✅ Container security scanning (recommended)

### Security Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Unauthorized camera access | User permission prompt, secure context |
| Data interception | HTTPS, encrypted S3 storage |
| Credential exposure | Environment variables, GitHub secrets |
| Container vulnerabilities | Regular image updates, security scanning |
| S3 data exposure | Bucket policies, private ACLs |

---

## 🐛 Troubleshooting

### Common Issues

**Camera not working:**
- Ensure HTTPS (localhost is exempt)
- Check browser permissions
- Verify camera hardware

**S3 upload fails:**
- Check AWS credentials
- Verify bucket permissions
- Check network connectivity

**Docker build fails:**
- Ensure Docker Desktop is running
- Check available disk space
- Verify Python version compatibility

**Deployment fails:**
- Verify GitHub secrets are set
- Check EC2 instance is running
- Confirm SSH key permissions

### Debug Mode

Enable debug logging:
```bash
export FLASK_DEBUG=true
python app.py
```

---

## 📊 Project Structure

```
camhack/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD
├── public/
│   ├── index.html              # Frontend UI
│   ├── styles.css              # Responsive styles
│   └── script.js               # Camera integration
├── app.py                      # Flask backend
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Local orchestration
├── download_from_s3.py         # S3 download script
├── delete_pics_from_s3.py      # S3 cleanup script
├── .env.example               # Environment template
├── .dockerignore              # Docker exclusions
└── README.md                  # This file
```

---

## 🤝 Contributing

This is an educational project for information security class. For contributions:

1. Fork the repository
2. Create a feature branch
3. Make security-conscious changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License & Disclaimer

**Educational Use Only**

This project is created for educational purposes in an information security course. It demonstrates security concepts and should not be used for any unauthorized surveillance or data collection.

**No Warranty**: This software is provided "as is" without warranty of any kind.

**Legal Compliance**: Ensure compliance with local privacy laws, GDPR, CCPA, and other data protection regulations.

**Ethical Use**: Always obtain explicit consent before capturing any images or data.

---

## 📞 Support

For questions about this educational project:
- Review the code comments
- Check the troubleshooting section
- Refer to the security considerations

**Remember**: This demonstrates security concepts - not how to bypass them!

---

*Created for Information Security class - Understanding web security through practical implementation*
