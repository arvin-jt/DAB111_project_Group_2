import sqlite3
import pandas as pd
import pathlib 

# Data Path (Database and Dataset Location) 
data_path = r'C:\Users\tamba\OneDrive\Documents\Repos\DAB111_project_Group_2\main\data'

# Function for creating Database and table from imported csv contents
def create_db(db_name, fname, tbl_name):

    # Set database location
    db_folder = data_path
    db = db_name
    db_path = pathlib.Path(db_folder) / db

    # Set csv file location
    csv_folder = data_path
    csv_name = fname
    csv_path = pathlib.Path(csv_folder) / csv_name

    # Set SQLite Connection and cursor 
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    # Read CSV file import in a pandas DataFrame
    titles = pd.read_csv(csv_path)

    # Insert the DataFrame into the SQLite database
    titles.to_sql(tbl_name, con, if_exists="replace", index=False)

    results = cursor.execute(f"SELECT * FROM {tbl_name}").fetchall()

    # Commit changes, Close connection and Return results
    con.commit()
    con.close()
    return results

# Select All function to retrieve  all records in titles table
def db_selectAll(path):
    # Establish connection and cursor
    con = sqlite3.connect(path)
    cursor = con.cursor()
    # Execute query
    results = cursor.execute("SELECT * FROM titles").fetchall()
    # Close connection and Return results
    con.close()
    return results

 # Function that returns database path and name 
def directory():
    base_path = pathlib.Path(data_path)
    db_name = "Titles"
    db_path = base_path / db_name
    return db_path





