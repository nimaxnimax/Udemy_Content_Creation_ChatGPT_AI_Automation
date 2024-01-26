import os
import openai

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
    prompt = input("Enter your prompt: ")
    print("You entered:", prompt)
    with open("chatgpt_api_key.txt", 'r') as file:
        api_key = file.readline().strip()
    openai.api_key = api_key
    zres = generate_response(prompt)
    print(f"{zres}")          
    with open("Output.txt", "a", encoding="utf-8") as file:
        file.write("**********" + "\n")
        file.write(prompt + "\n")
        file.write("**********" + "\n")
        file.write(zres + "\n")
        file.write("\n")
except:
    print("Error!")
