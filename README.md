# My Cloud Resume Challenge

This is how I created my static resume website to include tools and solutinos that a Cloud Engineer might use, including DNS, HTTPS, Python, IaC, CI/CD, AWS services such as Lambda, S3, API Gateway, DynamoDB, Route 53, Cloudfront, Certificate Manager, etc.

## 1. HTML
- What the resume is written in. Took a sample HTML template and included the resume information.
- filename is 'index.html'

## 2. CSS
- The resume style for the webpage.
- filename is 'style.css'

## 3. Static Website
- Static webpage is deployed on AWS S3 as static website.
- Include both 'index.html' and 'style.css' file in the S3 bucket
- Name of bucket is 'khanh-tran-cloud-resume'
- Enabled Static Website Hosting for S3 bucket, allow public access, and updated Bucket policy to allow GetObject for objectis in the S3 bucket for index.html

## 4. HTTPS
