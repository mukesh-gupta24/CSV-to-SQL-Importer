import os
import pandas as pd
from sqlalchemy import create_engine

# Set your SQL Server connection details
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
driver = 'SQL Server'  # Change this if you are using a different driver

# Create a connection string
conn_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Create a SQL Alchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

# Get a list of all CSV files in the folder
folder_path = 'your_folder_path'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[0]  # Use the CSV file name as the table name
    file_path = os.path.join(folder_path, csv_file)
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Write the DataFrame to the SQL Server database as a new table
    df.to_sql(table_name, engine, index=False, if_exists='append')
    print(f"Table '{table_name}' created in SQL Server.")

# Display a message indicating that all tables have been created
print("All tables have been created into SQL Server.")
