import requests
import os
from config import GROQ_API_KEY

class AIService:
    def __init__(self):
        self.api_key = GROQ_API_KEY
        self.base_url = 'https://api.groq.com/openai/v1'
        self.model = 'llama3-8b-8192'  # Note: Corrected from ollama3-8b-8192

    def generate_response(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': self.model,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 500
        }

        try:
            response = requests.post(f'{self.base_url}/chat/completions', json=data, headers=headers)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"Error generating AI response: {str(e)}"
