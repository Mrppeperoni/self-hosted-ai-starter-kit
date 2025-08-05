chat_openai.py

import openai
import os
from dotenv import load_dotenv

# Cargar la clave de la API desde un archivo .env (recomendado por seguridad)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Hacer una consulta al modelo GPT-4
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Eres un asistente amable y experto en Python."},
        {"role": "user", "content": "¿Cómo creo una función en Python?"}
    ]
)

# Mostrar respuesta
print("Respuesta de ChatGPT:")
print(response['choices'][0]['message']['content'])

