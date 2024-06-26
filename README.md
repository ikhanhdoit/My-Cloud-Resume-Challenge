# My Cloud Resume Challenge

This is how I created my static resume website to include tools and solutinos that a Cloud Engineer might use, including DNS, HTTPS, Python, IaC, CI/CD, AWS services such as Lambda, S3, API Gateway, DynamoDB, Route 53, Cloudfront, Certificate Manager, etc.

## 1. HTML
- What the resume is written in. Took a sample HTML template and included the resume information
- filename is 'index.html'

## 2. CSS
- The resume style for the webpage
- filename is 'style.css'

## 3. Static Website
- Static webpage is deployed on AWS S3 as static website
- Include both 'index.html' and 'style.css' file in the S3 bucket
- Name of bucket is 'khanh-tran-cloud-resume'
- Enabled Static Website Hosting for S3 bucket, allow public access, and updated Bucket policy to allow GetObject for objectis in the S3 bucket for index.html

## 4. HTTPS
- Register for the domain 'khanhtran0318.com' using Route53
- Used AWS Certification Manager to request public cert and store the SSL/TLS cert for HTTPS
- Created Cloudfront distribution to store and retrieve website at Edge locations to reduce latency
    - Then create Route53 CNAME records for the domain name to the Cloudfront distribution URL
    - Applied the SSL/TLS cert to Cloudfront distribute and redirect any HTTP to HTTPS
    - Updated S3 bucket policy to allow only GET from CloudFront