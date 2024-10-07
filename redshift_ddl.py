# pip install psycopg2-binary (if not download yet)
# Libraries import
import psycopg2

# Redshift Cluster connection details
with open(f"./env-config.cfg", 'r') as file:
    lines = file.readlines()
    host = lines[8].strip().split("= ")[1]
    port = lines[9].strip().split("= ")[1]
    dbname = lines[12].strip().split("= ")[1]
    user = lines[10].strip().split("= ")[1]
    password = lines[11].strip().split("= ")[1]
    schema = lines[13].strip().split("= ")[1]

# Connect to Redshift
try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True  # Automatically commit the transaction
    print("Connected to Redshift")

    # Create a Cursor object to interact with the database
    cur = conn.cursor()

    # Create Schema (optional)
    create_schema_sql = f"CREATE SCHEMA IF NOT EXISTS {schema};"
    cur.execute(create_schema_sql)
    print(f"Schema {schema} created successfully")

    # Do something here
    # Create stock indexes table
    # Create NVIDIA stock table
    create_nvidia_stock_table_query = '''
    CREATE TABLE IF NOT EXISTS nvidia_stock (
        date DATE NOT NULL PRIMARY KEY,
        open_price FLOAT,
        high_price FLOAT,
        low_price FLOAT,
        close_price FLOAT,
        adj_close_price FLOAT,
        volume BIGINT
    );
    '''
    cur.execute(create_nvidia_stock_table_query)
    print("Table 'nvidia_stock' created successfully.")

    # Create sentiment news table
    create_sentiment_news_table_query = '''
    CREATE TABLE IF NOT EXISTS sentiment_news (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        content TEXT,
        positive_score FLOAT,
        negative_score FLOAT,
        neutral_score FLOAT
    );
    '''
    cur.execute(create_sentiment_news_table_query)
    print("Table 'sentiment_news' created successfully.")

    # Close the Cursor and Connection
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error connecting to Redshift: {e}")
    exit()
