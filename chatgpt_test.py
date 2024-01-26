import os
import openai

prompt = "Hello. How are you?"

def generate_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": question},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return(result)

try:      
    file_name = "chatgpt_api_key.txt"
    with open(file_name, 'r') as file:
        api_key = file.readline().strip()
    openai.api_key = api_key
    zres = generate_response(prompt)
    print(f"{zres}")          
except:
    print("Error!")

