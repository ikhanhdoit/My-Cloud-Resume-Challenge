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
    - The origin domain is your S3 bucket URL and use the same S3 bucket URL to create the Origin Access Control (OAC) to allow origin access
    - Redirect HTTP to HTTPS for viewer protocol policy
    - Select the custom SSL certificate that you created with ACM
- Update S3 bucket policy to allow CloudFront s3:GetObject access that is provided to you by CloudFront
- Since index.html is inside the subfolder of 'frontend' in the S3 bucket, I had to make sure the Origin's 'Origin's path - optional' was updated to "frontend/"
    - This would ensure that cloudfront looks at that subfolder instead of looking on the root bucket and not find the index.html file
    - Also updated the Distrubition setting to make the 'Default root object - optional' to "index.html" so cloudfront would look at "frontend/index.html"

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
- ** After debugging the code and ensure that everything aligned together correctly, had to inspect the website because the old API URL was being invoked
    when the new one did not get invoked because of the CloudFront caching. Had to invalidate the CloudFront Distribution in order to have the visitor
    counter show up correctly on the webpage.

## 10. CI/CD (Part 1)
- Using Github Actions to create a CI/CD workflow where it will upload the latest updated files to the S3 bucket
- Create new AWS IAM Role to provide S3 bucket temporary access to upload files instead of creating the user
    - This is done using AWS IAM Roles and AWS Security Token Service (STS) to provide the Github Repository access to the S3 bucket
    - Need to also provide the permission policy to that role to upload objects into S3
- Then create the Github Actions and incorporate your role and S3 bucket into the YAML file in 'your-respository-name.github/workflows/'
- Now it will upload any new commits in the root (.) folder of Github to S3 by using aws s3 sync instead of just uploading everything in the repository each time

## 11. CI/CD (Part 2)
- Using Github Actions to show the most recent version of the resume by invalidating the Cloudfront Cache each time there is an update to Github
- This is ensure that users will get the most updated content instead of a cache when updates are made to GitHub

