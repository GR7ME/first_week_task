import os
import json
import gzip
import csv
import zipfile

# Function to extract JSON data from gzip and append it to a list
def extract_json(gzip_file_path):
    json_data_list = []
    with gzip.open(gzip_file_path, 'rt') as gz_file:
        for line in gz_file:
            json_data_list.append(json.loads(line))
    return json_data_list


# Function to convert JSON data list to CSV
def json_list_to_csv(json_data_list, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if json_data_list:
            # Write header
            csv_writer.writerow(json_data_list[0].keys())
            # Write data
            for row in json_data_list:
                csv_writer.writerow(row.values())

# Path to the zip file
zip_file_path = 'sample-data.zip'
# Path to the directory where you want to extract the files
extracted_folder_path = 'extracted_data'

# Extract the contents of the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# List to store JSON data from all files
all_json_data = []

# Iterate through the extracted folder to find gzip files
for root, dirs, files in os.walk(extracted_folder_path):
    for file in files:
        if file.endswith('.gz'):
            gzip_file_path = os.path.join(root, file)
            # Extract JSON data from gzip file and append it to the list
            all_json_data.extend(extract_json(gzip_file_path))

# Convert the combined JSON data list to CSV
csv_file_path = 'combined_data.csv'
json_list_to_csv(all_json_data, csv_file_path)

print("Combined CSV file created successfully.")


