# Import Libraries
from datetime import datetime, timedelta, timezone
from sentiment import sentiment
import pandas as pd
import json
import boto3
import sys
sys.stdout.reconfigure(encoding='utf-8')
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


# Fetch json file from S3 Bucket
def get_file_name_from_s3(s3_con, bucket, folder):
    file_name_list = []
    bucket = s3_con.Bucket(bucket)
    objects = bucket.objects.filter(Prefix=folder)
    for obj in objects:
        # Get the object key (file name)
        key = obj.key
        if not key.endswith('/'):
            file_name_list.append(key)
    return file_name_list


# Get content of file for further transform process
def get_content_file(s3_con, bucket, file_name):
    # Get the S3 object
    obj = s3_con.Object(bucket, file_name)

    # Handle type of file including json and csv
    if ('.json' in file_name): # Handle json file
        json_file = obj.get()['Body'].read().decode('utf-8')
        json_content = json.loads(json_file)
        return json_content
    
    else: # handle csv file
        # Read the CSV content directly into a DataFrame
        df = pd.read_csv(obj.get()['Body'])
        return df
    

# Group content file into json object and df for transform
def gather_content(file_name_list,s3_con, bucket):
    json_obj_list = []
    df = {}
    for file_name in file_name_list:
        if ('json' in file_name):
            temp_json = get_content_file(s3_con,bucket,file_name)
            json_obj_list.extend(temp_json)
        else:
            df = get_content_file(s3_con,bucket,file_name)
    return df, json_obj_list


# Transform with json file and csv file:
def transform(df,json_obj_list):
    # Transform with dataframe:
    # Handling Missing Data
    df = df.dropna()
    # Changing Data Types:
    df['Date']= pd.to_datetime(df['Date'])
    df['Open']= df['Open'].astype(float)
    df['High']= df['High'].astype(float)
    df['Low']= df['Low'].astype(float)
    df['Close']= df['Close'].astype(float)
    df['Adj Close']= df['Adj Close'].astype(float)
    df['Volume']= df['Volume'].astype(int)
    # Rename Adj Close to Adj_Close
    df.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)

    # Transform with json list and perform sentiment analysis with json:
    sentiment_list = sentiment(json_obj_list)
    return df, sentiment_list


# Upload data to S3 Bucket
def upload_to_s3(conn,file_name, bucket_name, file_name_in_s3):
    """Upload file to S3 Bucket"""
    conn.meta.client.upload_file(
        Filename=file_name, 
        Bucket=bucket_name, 
        Key=file_name_in_s3
    )

# Main process
def upload(conn,bucket_name):
    local_folder = r'D:\DataLearning\Projects\sentiment-analysis-ndivia-stock-prediction\data\transformed_data' # replace with your own local path to this folder
    # Iterate through the files in the local folder
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            # Create the full local path
            local_file_path = os.path.join(root, file)

            try:
                # Upload the file to S3
                upload_to_s3(conn, local_file_path, bucket_name, f"transformed/{file}")
                print(f'Successfully uploaded ./data/transformed_data/{file} to s3://{bucket_name}/transformed/{file}')
            except Exception as e:
                print(f'Error uploading {local_file_path}: {str(e)}')

# Main process
def main():
    # S3 Bucket config
    config = s3_config()

    # S3 Bucker connection
    conn = s3_connect(config)

    # Get all file name in raw_data
    file_name_list = get_file_name_from_s3(conn, config['bucket_name'],'raw_data/')

    # Gather content file into a dataframe and list of json news:
    df, json_obj_list = gather_content(file_name_list,conn,config['bucket_name'])

    # Perform transform including clean and sentiment
    stock_index_df, sentiment_list = transform(df,json_obj_list)

    # Display result:
    print(f"Number of sentiment news")
    print(len(sentiment_list))
    print(f"\nExample of the sentiment news")
    print(f"Date: {sentiment_list[0]['Date']}")
    print(f"Content: {sentiment_list[0]['Content']}")
    print(f"Positive Score: {sentiment_list[0]['Positive']}")
    print(f"Negative Score: {sentiment_list[0]['Negative']}")
    print(f"Neutral Score: {sentiment_list[0]['Neutral']}")
    print(f"\nFirst 5 rows of dataframe")
    print(stock_index_df.head())

    # Save df and sentiment news into file for further analysis and model training
    # For nvidia stock:
    print(f"\nSave Nvidia Indexes into nvidia_indexes.csv file")
    stock_index_df.to_csv(f"./data/transformed_data/nvidia_indexes.csv", index=False)

    # For sentiment news:
    # Convert the list of JSON objects to a DataFrame
    sentiment_news_df = pd.DataFrame(sentiment_list)
    # Save the DataFrame to a CSV file
    print(f"Save Sentiment News into sentiment_news.csv file")
    sentiment_news_df.to_csv('./data/transformed_data/sentiment_news.csv', index=False, encoding='utf-8', errors='replace')

    # Upload into S3 bucker with transformed folder
    print("")
    upload(conn,config['bucket_name'])
    
# Run file
if __name__ == "__main__":
    print(f"Starting transform process...")
    main()
    print(f"Transform process finished.")