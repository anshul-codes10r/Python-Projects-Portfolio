import os
from dotenv import load_dotenv
import webbrowser
import requests
import sys
from time import sleep
load_dotenv(dotenv_path=".env", override=True)

def typ(text): #typ() = typing_effect
    for char in text:
        sleep(0.07)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def intro():    
    print("╔══════════════════════════════╗")
    print("║                               ║")
    typ("║        🤖 AVENYA AI           ║")
    print("║  ------------------------        ║")
    typ("║     AI TEXT ASSISTANT         ║")
    print("║                               ║")
    print("╚══════════════════════════════╝")
    print("╔══════════════════════════════╗")
    print("║                               ║")
    typ("║• NAME   :   AVENYA            ║")
    typ("║• CREATOR   :   ANSHUL-CODES   ║")
    typ("║• LANGUAGE   :   PYTHON🐍         ║")
    typ("║• CREATED   :   AUGUST 6, 2026 ║")
    typ("║• STATUS   :   ONLINE🟢        ║")
    print("║                               ║")
    print("╚══════════════════════════════╝")    
intro()        

def get_command():
    command = input("Avenya > How can I assist you? ")
    return command

def command_validation(command):
    known_commands = [
            "Avenya open google",
            "Avenya open youtube",
            "Avenya open chatgpt",
            "Avenya open github",
            "Help",
            "About Avenya",
            "Exit"
    ]
    if command in known_commands:
        return "command"
    return "ai"

def execute_command(command):
    
    if command == "Help":
        print("I can open Google, YouTube, Chatgpt and GitHub, provide information about Avenya, and answer many basic questions.\nType a command and I’ll assist you.\nWhenever you want Avenya to perform a task, start your command with Avenya.")
    
    elif command == "About Avenya":
        print("I am Avenya, your AI text assistant.\nI was created by Anshul on August 6, 2026, using Python.\nI can handle basic commands, open Google, Youtube, Chatgpt & Github websites, and answer many basic questions.\nTo ask Avenya to perform a task, always start your command with Avenya.")
    
    elif command == "Avenya open google":
        webbrowser.open("https://www.google.com")
        print("Google opened.")   
    
    elif command == "Avenya open youtube":
        webbrowser.open("https://www.youtube.com")
        print("Youtube opened")
    
    elif command == "Avenya open chatgpt":
        webbrowser.open("https://chatgpt.com")
        print("Chatgpt opened")         
    
    elif command == "Avenya open github":
        webbrowser.open("https://www.github.com")
        print("Github opened")
    
    elif command == "Exit":
        print("Thank you for using Avenya. Goodbye! 👋")        
        return True
    return False                          

def handle_ai(command):
    try:        
        base_url = "https://api.groq.com/openai/v1"
        url = base_url + "/chat/completions"
        api_key = os.getenv("GROQ_API_KEY")
        headers = {
                "Authorization" : f"Bearer {api_key}",
                "Content-Type" : "application/json"
        }  
        data = {
                "model" : "llama-3.3-70b-versatile",
                "messages" : [
                    {
                        "role" : "user",
                        "content" : command
                     }
                  ]
        }                        
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout = 15
        )
        response.raise_for_status()
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        print(f"\nAvenya > {answer}")
    except requests.RequestException:
        print("Sorry, Avenya couldn't connect to the AI service.")

while True:
    command = get_command()
    result = command_validation(command)
    if result == "command":
        should_exit = execute_command(command)
        if should_exit:
            break
    else:
        handle_ai(command)                                                                               