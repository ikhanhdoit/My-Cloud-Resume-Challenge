# My Cloud Resume Challenge

This is how I created my static resume website to include tools and solutinos that a Cloud Engineer might use, including DNS, HTTPS, Python, IaC, CI/CD, AWS services such as Lambda, S3, API Gateway, DynamoDB, Route 53, CloudFront, Certificate Manager, etc. ChatGPT was used to help with steps and debugging code.

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
- Since we are using CloudFront as our CDN and will map the website domain to CloudFront, we don't need to enable Static Website Hosting for S3 bucket, allow public access, and updated Bucket policy to allow GetObject for objectis in the S3 bucket for index.html. We leave all of those disabled.
    - This means that the bucket and index.html object does not have public access

## 4. HTTPS
- Register for the domain 'khanhtran0318.com' using Route53
- Used AWS Certification Manager (ACM) to request public cert and store the SSL/TLS cert for HTTPS
- Created CloudFront distribution to store and retrieve website at Edge locations to reduce latency
    - The origin domain is your s3 bucket URL and use the same s3 bucket URL to create the Origin Access Control (OAC) to allow origin access
    - Redirect HTTP to HTTPS for viewer protocol policy
    - Select the custom SSL certificate that you created with ACM
- Update S3 bucket policy to allow CloudFront s3:GetObject access that is provided to you by CloudFront

## 5. DNS
- Then create Route53 A record aliases for the domain name (both with and without www) to the CloudFront distribution URL

## 6. Javascript
- Use javascript scripts for mobile menu and visitor counter

## 7. DynamoDB
- Use AWS DynamoDB to store and update the count on the database

## 8. Lambda
- Using and AWS Lambda function (in Python) to update the visitor count to DynamoDB

## 9. API Gateway
- Use AWS API Gateway to create an REST API to communicate frontend website with the backend infrastructure
- This will get and update the visitor count for the resume website
- Use API Gateway to GET the AWS Lambda to get invoked each time a visitor comes to the website
- This will update and GET the count of visitors from DynamoDB



