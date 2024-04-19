import sqlite3
import pandas as pd
import pathlib 

# Data Path (Database and Dataset Location)
data_path = r'C:\Users\tamba\OneDrive\Documents\Repos\DAB111_project_Group_2\main\data'

def create_db(db_name, fname, tbl_name):

    # Specify the full path to the SQLite database file
    db_folder = data_path
    db = db_name
    db_path = pathlib.Path(db_folder) / db

    # Specify the full path to the CSV file
    csv_folder = data_path
    csv_name = fname
    csv_path = pathlib.Path(csv_folder) / csv_name

    # Connect to the SQLite database
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    # Read the CSV file into a pandas DataFrame
    titles = pd.read_csv(csv_path)

    # Insert the DataFrame into the SQLite database
    titles.to_sql(tbl_name, con, if_exists="replace", index=False)

    results = cursor.execute(f"SELECT * FROM {tbl_name}").fetchall()

    con.commit()
    con.close()
    return results

def db_selectAll(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    results = cursor.execute("SELECT * FROM titles").fetchall()
    con.close()
    return results


 
def directory():
    base_path = pathlib.Path(data_path)
    db_name = "Titles"
    db_path = base_path / db_name
    return db_path





