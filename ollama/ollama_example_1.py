import requests

def chat_with_me(txt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.2", 
        "format": "json", 
        "prompt": txt,
        "stream": False,
        "options": { "temperature": 0 } 
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["response"]

# Example usage:
while True:
    txt = input("\n>>> ")

    if txt == "q":
        break
    
    response = chat_with_me(txt)
    print(response)
