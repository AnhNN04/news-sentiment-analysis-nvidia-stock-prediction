# Import libraries
import boto3
import botocore
import os

# S3 Bucket configuration
def s3_config():
    with open(f"./env-config.cfg",'r') as file:
        lines = file.readlines()
        s3_config = {
            'access_key' : lines[2].strip().split('= ')[1],
            'secret_key' : lines[3].strip().split('= ')[1],
            'region' : lines[4].strip().split('= ')[1],
            'bucket_name' : lines[5].strip().split('= ')[1],
            'service_name' : lines[6].strip().split('= ')[1]
        }
    return s3_config

# S3 Bucket connect
def s3_connect(s3_config):
    """Connect to S3 Instance"""
    try:
        conn = boto3.resource(
            service_name=s3_config['service_name'],
            region_name=s3_config['region'],
            aws_access_key_id=s3_config['access_key'],
            aws_secret_access_key=s3_config['secret_key']
            )
        print(f"Connected to S3 Bucket")
        return conn
    except Exception as e:
        print(f"Can't connect to S3. Error: {e}")

# Upload data to S3 Bucket
def upload_to_s3(conn,file_name, bucket_name, file_name_in_s3):
    """Upload file to S3 Bucket"""
    conn.meta.client.upload_file(
        Filename=file_name, 
        Bucket=bucket_name, 
        Key=file_name_in_s3
    )

# Main process
def main():
    local_folder = r'D:\DataLearning\Projects\sentiment-analysis-ndivia-stock-prediction\data\raw_data\data_to_s3' # replace with your own local path to this folder
    bucket_config = s3_config()
    bucket_name = bucket_config['bucket_name']
    conn = s3_connect(bucket_config)

    # Iterate through the files in the local folder
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            # Create the full local path
            local_file_path = os.path.join(root, file)

            try:
                # Upload the file to S3
                upload_to_s3(conn, local_file_path, bucket_name, f"raw_data/{file}")
                print(f'Successfully uploaded ./data/raw_data/data_to_s3/{file} to s3://{bucket_name}/raw_data/{file}')
            except Exception as e:
                print(f'Error uploading {local_file_path}: {str(e)}')

if __name__ == "__main__":
    print(f"Starting upload data into S3 Bucket...")
    main()
    print(f"Process finished.")