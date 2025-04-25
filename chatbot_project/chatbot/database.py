import pyodbc
import config
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def connect_to_db():
    conn = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={config.DB_SERVER};DATABASE={config.DB_DATABASE};UID={config.DB_USERNAME};PWD={config.DB_PASSWORD}'
    )
    return conn

def fetch_all_tables_and_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
    )
    tables = [row[0] for row in cursor.fetchall()]

    table_data = {}
    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        table_data[table] = {"columns": columns, "rows": rows}

    conn.close()
    return table_data
