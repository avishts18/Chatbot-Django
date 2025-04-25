import config

def create_prompt_from_tables(table_data, user_query):
    prompt = "The following is data from the database 'NewVehiclesTable':\n\n"

    for table_name, data in table_data.items():
        columns = data["columns"]
        rows = data["rows"]
        data_str = "\n".join(
            [", ".join(f"{col}: {value}" for col, value in zip(columns, row)) for row in rows]
        )
        prompt += f"Table: {table_name}\nColumns: {', '.join(columns)}\nData:\n{data_str}\n\n"

    prompt += f"Answer the following question based on the above data: {user_query}"
    return prompt
