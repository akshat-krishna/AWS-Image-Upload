from flask import Flask, request, render_template, redirect, url_for
import boto3

app = Flask(__name__)

S3_BUCKET = 'mid-term-image-bucket' # S3 BUCKET NAME
s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    if 'Mozilla' in user_agent: 
        return render_template('midTermUploadImage.html')
    else:
        return 'Hello user!'

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'File not added'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'File not added'

    try:
        s3.upload_fileobj(file, S3_BUCKET, file.filename)
        return redirect(url_for('display_data', filename=file.filename))
    
    except Exception as e:
        return f'Error uploading image: {str(e)}'
    
@app.route('/display-data/<filename>')
def display_data(filename):
    response = dynamodb.get_item(
            TableName='mid-term-image-table', # Dynamo DB table name
            Key={
                'file-name': {'S': filename}
            }
        )
    
    item = response.get('Item')
    return render_template('midTermImageDetails.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
