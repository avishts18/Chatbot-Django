from django.http import JsonResponse
from . import openai_integration, database, create_prompt

def query_chatbot(request):
    user_query = request.GET.get('query', '')
    
    if user_query:
        table_data = database.fetch_all_tables_and_data()
        prompt = create_prompt.create_prompt_from_tables(table_data, user_query)
        response = openai_integration.query_openai_model(prompt)
        return JsonResponse({"response": response})
    else:
        return JsonResponse({"error": "No query provided"}, status=400)
