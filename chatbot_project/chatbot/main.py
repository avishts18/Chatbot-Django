import openai_integration
import database
import create_prompt
import config

def main():
    while True:
        user_input = input("Ask me anything about the Vehicle Details: ")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        table_data = database.fetch_all_tables_and_data()
        prompt = create_prompt.create_prompt_from_tables(table_data, user_input)
        response = openai_integration.query_openai_model(prompt)

        print("Response:", response)

if __name__ == "__main__":
    main()
