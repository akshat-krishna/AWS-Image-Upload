

# E-Bike Image Upload and Metadata Management

## Overview
This project is a web application for an e-bike company, designed to facilitate the management of image uploads and metadata. It allows users to upload images to an AWS S3 bucket, and then stores the image metadata in an AWS DynamoDB table. The frontend is built with HTML and communicates with the backend Flask server, which interacts with AWS services.

## Features
- Image upload functionality through a web interface.
- Direct upload of images to AWS S3.
- Metadata extraction and storage in AWS DynamoDB.
- Simple frontend to display uploaded image metadata.

## Technologies
- **Frontend:** HTML, JavaScript
- **Backend:** Python with Flask
- **Database:** AWS DynamoDB
- **Storage:** AWS S3
- **Testing:** Pytest

### Prerequisites
- Python 3.x
- AWS account with access to S3 and DynamoDB
- Flask
- Boto3
- Pytest (for testing)

## Configuration

To configure the application for your AWS environment, update the following in `connect.py`:

- `S3_BUCKET`: Your AWS S3 bucket name.
- `DYNAMO_TABLE`: Your AWS DynamoDB table name.
