import openai
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config

openai.api_key = config.OPENAI_API_KEY

def query_openai_model(prompt, temperature=0.0):
    try:
      
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            #  model="gpt-3.5 turbo", 
             
            messages=[{"role": "system", "content": "You are a helpful assistant. Provide accurate answers based on the data given."},
                      {"role": "user", "content": prompt}],
            temperature=temperature 
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
