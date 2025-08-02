import requests

def ollama_chat(prompt, model="llama3.1:8b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", f"[Error] Unexpected API response: {data}")
    except requests.exceptions.RequestException as e:
        return f"[Request error] {str(e)}"
