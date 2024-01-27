import os
import openai
import time
import datetime
import random
file_name = "chatgpt_api_key.txt"
with open(file_name, 'r') as file:
    api_key = file.readline().strip()
openai.api_key = api_key
zquit = False
def generate_response(question):
    try:
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
    except ValueError:
        result = 'ChatGPT Server Error Connecting or Generating!'
    return(result)
def remove_old_data():
    file_names = ["Result_Title.txt", "Result_Introduction.txt", "Result_Body_Social.txt", "Result_Body_Article.txt", "Result_Conclusion.txt", "Result_CTA.txt", "Result_Hashtag.txt", "Result_Auto_Generated.txt"]
    for file_name in file_names:
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write("")
print("************************************************")
print('Started!')
if input("Remove Old Data Saved in TXT Files? (y/n): ").lower() == 'y':
    remove_old_data()
    print("Removed - Done!")
else:
    print("No changes made.")
zquit = False
print("************************************************")
q0 = input("Auto Generate Content With Optimal Word or Character Count For Each Section (y/n): ").lower()
if q0 == 'y':
    zfilenametosave = "Result_Auto_Generated.txt"
    input_text = input("Enter Keywords or Subject for Your Content: ")
    if input_text.strip():
        print("Ok")
        question = input_text
        while True:
            print("Generating Content - Wait...")
            prompt = "give me a body for blog post between 250 to 500 words and do not mention number of words and the topic is about" + question
            zres = ""
            zres = generate_response(prompt)
            print("")
            print(f"{zres}")
            with open(zfilenametosave, "a", encoding="utf-8") as file:
                file.write("**** Content For Your Subject/Keywords/Question >> " + question + "\n")
                file.write(zres + "\n")
                file.write("\n")
            time.sleep(0)
            prompt = "give me a body for social media content between 50 to 100 words seperate each social media and the topic is about " + question
            zres = ""
            zres = generate_response(prompt)
            print("")
            print(f"{zres}")
            with open(zfilenametosave, "a", encoding="utf-8") as file:
                file.write(zres + "\n")
                file.write("\n")
            time.sleep(0)
            prompt = "give me a call-to-action CTA from 10 to 20 words and hashtags seperate each social media and the topic is about " + question
            zres = ""
            zres = generate_response(prompt)
            print("")
            print(f"{zres}")
            with open(zfilenametosave, "a", encoding="utf-8") as file:
                file.write(zres + "\n")
                file.write("\n")
            time.sleep(0)
            print("")
            print("Done! - Results saved in file >> " + zfilenametosave)
            print("************************************************")
            zloop = input("Need More Auto Generated Data? (y/n): ").lower()
            if zloop != 'y':
                break        
    else:
        print("Error: Please enter your subject or keywords. Try again.")
zquit = False
print("************************************************")
q1 = input("Data For >> Title/Headline? (y/n): ").lower()
if q1 == 'y': 
    zfilenametosave = "Result_Title.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Words for >> Title/Headline (5-20): "))
                if 5 <= num_characters <= 20:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Title: ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give 10 titles each title from 5 to {num_characters} words about " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Title/Headline for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Title/Headline? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break                                   
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 5 and 20. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
zquit = False
print("************************************************")
q2 = input("Data For >> Introduction? (y/n): ").lower()
if q2 == 'y':
    zfilenametosave = "Result_Introduction.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Words for >> Introduction (100-200): "))
                if 100 <= num_characters <= 200:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Introduction: ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give 5 short introduction for my article each introduction from 100 to {num_characters} words about " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Introduction for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Introduction? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 100 and 200. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
zquit = False
print("************************************************")
q3 = input("Data For Social Media >> Body(Main Points and Supporting Details)? (y/n): ").lower()
if q3 == 'y':   
    zfilenametosave = "Result_Body_Social.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Words for >> Social Media Body (50-150): "))
                if 50 <= num_characters <= 150:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Body (Social Media): ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give 5 content for body for my social media post each body from 50 to {num_characters} words about " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Social Media Body for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Social Media Body? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break                                   
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 50 and 150. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
zquit = False
print("************************************************")
q4 = input("Data For Blog Post or Article >> Body(Main Points and Supporting Details)? (y/n): ").lower()
if q4 == 'y':
    zfilenametosave = "Result_Body_Article.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Words for >> Blog Post or Article (200-500): "))
                if 200 <= num_characters <= 500:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Body (Blog Post or Article): ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give 5 content for body for my blog post or article each body from 200 to {num_characters} words and do not mention number of words and the topic is about " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Blog Post or Article Body for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Blog Post or Article? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break                                    
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 200 and 500. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
zquit = False
print("************************************************")
q5 = input("Data For >> Conclusion? (y/n): ").lower()
if q5 == 'y':
    zfilenametosave = "Result_Conclusion.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Words for >> Conclusion (50-200): "))
                if 50 <= num_characters <= 200:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Conclusion: ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give 5 conclusion for my blog post or article each conclusion from 50 to {num_characters} words about " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Conclusion for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Conclusion? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 50 and 200. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
zquit = False
print("************************************************")
q6 = input("Data For >> Call-to-Action (CTA)? (y/n): ").lower()
if q6 == 'y':   
    zfilenametosave = "Result_CTA.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Words for >> Call-to-Action (CTA) (5-20): "))
                if 5 <= num_characters <= 20:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Call-to-Action (CTA): ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give 5 Call-to-Action (CTA) for my blog post or article each Call-to-Action (CTA) from 5 to {num_characters} words about " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Call-to-Action (CTA) for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Call-to-Action (CTA)? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 5 and 20. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
zquit = False
print("************************************************")
q7 = input("Data For >> Hashtag? (y/n): ").lower()
if q7 == 'y':   
    zfilenametosave = "Result_Hashtag.txt"
    while True:
        if zquit == False:
            try:
                num_characters = int(input("Enter Number of Hashtags (3-10): "))
                if 3 <= num_characters <= 10:
                    print("Ok")
                    while True:
                        if zquit == False:
                            input_text = input("Enter Keywords or Subject for >> Hashtags: ")
                            if input_text.strip():
                                print("Ok")
                                question = input_text
                                prompt = "Give {num_characters} Hashtag for my blog post or article for Instagram and Twitter and Facebook and LinkedIn each social media seperate about topic " + question
                                zloop = "y"
                                while True:
                                    try:
                                        print("Wait...")
                                        zres = ""
                                        zres = generate_response(prompt)
                                        print("************************************************")
                                        print(f"{zres}")
                                        with open(zfilenametosave, "a", encoding="utf-8") as file:
                                            file.write("**** Hashtags for Subject or Keywords >> " + question + "\n")
                                            file.write("\n")
                                            file.write(zres + "\n")
                                            file.write("\n")
                                        time.sleep(0)
                                        print("************************************************")
                                        print("Done! - Results saved in file >> " + zfilenametosave)
                                    except ValueError:
                                        print("Rate limit reached on requests per min (RPM): Limit 3 - Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.")
                                    print("************************************************")
                                    zloop = input("Need More Data for >> Hashtag? (y/n): ").lower()
                                    if zloop != 'y':
                                        zquit = True
                                        break
                            else:
                                print("Error: Please enter your subject or keywords. Try again.")
                        else:
                            break
                else:
                    print("Error: Please enter a number between 3 and 10. Try again.")
            except ValueError:
                print("Error: Please enter a valid number. Try again.")
        else:
            break
