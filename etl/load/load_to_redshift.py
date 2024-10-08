import boto3
import psycopg2

# Step 1: Define the S3 and Redshift connection details
with open(f"./env-config.cfg",'r') as file:
    lines = file.readlines()

    s3_bucket = lines[5].strip().split('= ')[1]
    s3_key_1 = "transformed/nvidia_indexes.csv"
    s3_key_2 = "transformed/sentiment_news.csv"
    s3_region = lines[4].strip().split('= ')[1] # Change based on your region

    redshift_host = lines[8].strip().split('= ')[1]
    redshift_port = lines[9].strip().split('= ')[1]
    redshift_dbname = lines[12].strip().split('= ')[1]
    redshift_user = lines[10].strip().split('= ')[1]
    redshift_password = lines[11].strip().split('= ')[1]
    redshift_table_1 = lines[15].strip().split('= ')[1]
    redshift_table_2 = lines[16].strip().split('= ')[1]

    iam_role_arn = lines[14].strip().split('= ')[1]

# Step 2: Connect to Redshift
try:
    conn = psycopg2.connect(
        host=redshift_host,
        port=redshift_port,
        dbname=redshift_dbname,
        user=redshift_user,
        password=redshift_password
    )
    cur = conn.cursor()
    print("Connected to Redshift")

    # Step 3: Execute the COPY command to load data from S3 to Redshift
    copy_query = f"""
    COPY {redshift_table_1}
    FROM 's3://{s3_bucket}/{s3_key_1}'
    IAM_ROLE '{iam_role_arn}'
    REGION '{s3_region}'
    CSV
    IGNOREHEADER 1;
    """  # Modify this query depending on the data format (CSV, JSON, etc.)

    cur.execute(copy_query)
    conn.commit()
    print(f"Data loaded successfully from S3 to {redshift_table_1}")

    # Step 3: Execute the COPY command to load data from S3 to Redshift
    copy_query = f"""
    COPY {redshift_table_2}
    FROM 's3://{s3_bucket}/{s3_key_2}'
    IAM_ROLE '{iam_role_arn}'
    REGION '{s3_region}'
    CSV
    IGNOREHEADER 1;
    """  # Modify this query depending on the data format (CSV, JSON, etc.)

    cur.execute(copy_query)
    conn.commit()
    print(f"Data loaded successfully from S3 to {redshift_table_2}")

except Exception as e:
    print(f"Error: {e}")

finally:
    cur.close()
    conn.close()
