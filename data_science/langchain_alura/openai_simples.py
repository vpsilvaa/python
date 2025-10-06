from openai import OpenAI
from dotenv import load_dotenv
import warnings
import os

load_dotenv()
#warnings.filterwarnings("ignore", category=UserWarning)

numero_dias = 7
numero_criancas = 5
atividade = 'praia'

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma família com {numero_criancas} crianças, que gostam de {atividade}."
#print(prompt)

client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'))

resposta = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant'},
        {'role': 'user', 'content': prompt}
    ]
)

resposta = resposta.choices[0].message.content
print(resposta)