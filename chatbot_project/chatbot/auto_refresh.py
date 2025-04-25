import hashlib
import time
from database import fetch_all_tables_and_data

def get_data_hash():
    table_data = fetch_all_tables_and_data()
    hash_data = ""
    for table_name, data in table_data.items():
        columns = data["columns"]
        rows = data["rows"]
        data_str = "\n".join(
            [", ".join(f"{col}: {value}" for col, value in zip(columns, row)) for row in rows]
        )
        hash_data += f"Table: {table_name}\nColumns: {', '.join(columns)}\nData:\n{data_str}\n"

    return hashlib.sha256(hash_data.encode('utf-8')).hexdigest()

def auto_refresh():
    last_hash = get_data_hash()
    while True:
        current_hash = get_data_hash()
        if current_hash != last_hash:
            print("Data has changed, refreshing model data.")
            last_hash = current_hash

        time.sleep(60) 
