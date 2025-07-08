import requests
from gtts import gTTS

OLLAMA_URL = "http://localhost:11434/api/generate"

def generateText(player_name):
    # Hardcoded prompt
    prompt = f"Write a short summary about {player_name}"

    # Request payload for Ollama
    payload = {
        "model": "llama3.2",  
        "prompt": prompt,
        "stream": False 
    }

    # Send POST request
    response = requests.post(OLLAMA_URL, json=payload)

    # Robustly get the text
    result = response.json()
    if 'response' in result:
        print("\nGenerated Summary:\n")

        tts = gTTS(result['response'])
        file_name=f"{player_name.replace(' ', '_')}.mp3"
        tts.save(file_name)
        return file_name
    else:
        print("Oops! 'response' key not found.")
        return None
