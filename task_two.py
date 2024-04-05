import csv
import mysql.connector

# Function to read CSV file and insert data into MySQL database
def insert_data_from_csv(csv_file_path):
    # MySQL connection parameters
    db_config = {
        'host': '172.18.0.3',
        'user': 'root',
        'password': 'rootpassword',
        'database': 'mydb'
    }

    # Connect to MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = ('''CREATE TABLE IF NOT EXISTS work_mock (
                bCls INT,
                bC VARCHAR(10),
                bCT VARCHAR(10),
                negA INT,
                npi BIGINT,
                tin BIGINT,
                tinT INT,
                zip INT,
                negT FLOAT,
                negR INT,
                posH INT,
                mdH INT,
                nrP INT,
                _dT INT
            );
            ''')
    cursor.execute(query)
    connection.commit()

    try:
        # Open CSV file
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row if exists

            # Iterate over CSV data and insert into MySQL
            for row in csv_reader:
                # Assuming the table has columns col1, col2, col3
                print(row)
                query = """INSERT INTO work_mock (bCls, bC, bCT, negA, npi, tin, tinT, zip, negT, negR, posH, mdH, nrP, _dT) VALUES (%s, %s,
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, tuple(row))

        # Commit the transaction
        connection.commit()
        print("Data inserted successfully.")

    except Exception as e:
        # Rollback the transaction if an error occurs
        print("Error:", e)
        connection.rollback()

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

# Path to the CSV file
csv_file_path = 'combined_data.csv'

# Call the function to insert data from CSV into MySQL database
insert_data_from_csv(csv_file_path)
