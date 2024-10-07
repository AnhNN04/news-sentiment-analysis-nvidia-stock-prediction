# This file is for convert from txt file into json file with each json object contain Date and Content
# This step will loop through all clean_news and perform some actions to join string, modify date and add into json file

# Libs import:
from datetime import datetime
import re
import json

# Read txt file and perform some action and return list of json object
# Turn date into formar 'YYYY-MM-DD'

def convert_to_json_f1(file1):
    with open(file1, 'r', encoding='utf-8',errors='ignore') as file:
        news_str = str(file.read())
    # Split the input data into blocks
    news_list = re.split(r'\n(?=\d{2}-\d{2}-\d{4})', news_str.strip())
    # List to store News objects
    news_object_list = []
    # Process each entry
    for news in news_list:
        news_obj = {}
        # Separate the date from the content
        lines = news.split('\n', 1)
        date_str = lines[0].strip()  # First line is the date
        content = lines[1].strip().replace('\n', '. ')   # Remaining text is the content

        # Create an New object and add it to the list
        news_obj['Date'] = date_str
        news_obj['Content'] = content
        news_object_list.append(news_obj)

    return news_object_list

def convert_to_json_f2(file2):
    with open(file2, 'r', encoding='utf-8',errors='replace') as file:
        news_str = str(file.read())
    # Split the input data into blocks
    news_list = re.split(r'\n\s*\n', news_str.strip())
    # List to store News objects
    news_object_list = []
    # Process each entry
    for news in news_list:
        news_obj = {}
        # Separate the date from the content
        lines = news.rsplit('\n', 1)
        content = lines[0].strip().replace('\n', '. ')  # First line is the content because using rsplit instead of split   
        date_str = lines[1].strip()   # Remaining text is the date

        # Create an New object and add it to the list
        news_obj['Date'] = date_str
        news_obj['Content'] = content
        news_object_list.append(news_obj)

    return news_object_list

def convert_to_json_f3(file3):
    with open(file3, 'r', encoding='utf-8',errors='replace') as file:
        news_str = str(file.read())

    # Split the input data into lines
    lines = news_str.strip().split('\n')

    # List to store news objects
    news_object_list = []

    # Process each line
    for i in range(0, len(lines), 2):
        content = lines[i].strip().replace('\n', '. ')  # Content (even index)
        date_str = lines[i + 1].strip()  # Date (odd index)
        
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        date_str = date_obj.strftime('%m-%d-%Y')

        # Create an New object and add it to the list
        news_obj = {}
        news_obj['Date'] = date_str
        news_obj['Content'] = content
        news_object_list.append(news_obj)

    return news_object_list

def convert_to_json_f4(file4):
    with open(file4, 'r', encoding='utf-8',errors='replace') as file:
        news_str = str(file.read())
    # Split the input data into blocks
    news_list = re.split(r'\n\s*\n', news_str.strip())
    # List to store News objects
    news_object_list = []
    # Process each entry
    for news in news_list:
        news_obj = {}
        # Separate the date from the content
        lines = news.split('\n', 1)
        content = lines[1].strip().replace('\n','. ')  # First line is the date 
        date_str = lines[0].strip()   # Remaining text is the content

        # Create an New object and add it to the list
        news_obj['Date'] = date_str
        news_obj['Content'] = content
        news_object_list.append(news_obj)

    return news_object_list

def convert_to_json_f5(file5):
    with open(file5, 'r', encoding='utf-8',errors='replace') as file:
        news_str = str(file.read())
    # Split the input data into blocks
    news_list = re.split(r'\n\s*\n', news_str.strip())
    # List to store News objects
    news_object_list = []
    # Process each entry
    for news in news_list:
        news_obj = {}
        # Separate the date from the content
        lines = news.rsplit('\n', 1)
        content = lines[0].strip().replace('\n','. ')  # First line is the content
        date_str = lines[1].strip()   # Remaining text is the date

        # Create an New object and add it to the list
        news_obj['Date'] = date_str
        news_obj['Content'] = content
        news_object_list.append(news_obj)

    return news_object_list


def main():
    news_1 = convert_to_json_f1(f"./data/raw_data/preprocess_data/news_1_clean.txt")
    with open(f"./data/raw_data/data_to_s3/json_news_1.json", 'w') as file:
            json.dump(news_1, file, indent=4)
    print(f"Finished file news_1.")

    news_2 = convert_to_json_f2(f"./data/raw_data/preprocess_data/news_2_clean.txt")
    with open(f"./data/raw_data/data_to_s3/json_news_2.json", 'w') as file:
            json.dump(news_2, file, indent=4)
    print(f"Finished file news_2.")

    news_3 = convert_to_json_f3(f"./data/raw_data/preprocess_data/news_3_clean.txt")
    with open(f"./data/raw_data/data_to_s3/json_news_3.json", 'w') as file:
            json.dump(news_3, file, indent=4)
    print(f"Finished file news_3.")

    news_4 = convert_to_json_f4(f"./data/raw_data/preprocess_data/news_4_clean.txt")
    with open(f"./data/raw_data/data_to_s3/json_news_4.json", 'w') as file:
            json.dump(news_4, file, indent=4)
    print(f"Finished file news_4.")

    news_5 = convert_to_json_f5(f"./data/raw_data/preprocess_data/news_5_clean.txt")
    with open(f"./data/raw_data/data_to_s3/json_news_5.json", 'w') as file:
            json.dump(news_5, file, indent=4)
    print(f"Finished file news_5.")

if __name__ == "__main__":
    print(f"Starting convert News into json file...")
    main()
    print(f"Finished Converting.")

