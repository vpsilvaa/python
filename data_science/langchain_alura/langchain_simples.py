from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import warnings
import os

load_dotenv()
warnings.filterwarnings("ignore", category=UserWarning)

numero_dias = 7
numero_criancas = 5
atividade = 'praia'

model_prompt = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma família com {criancas} crianças, que gostam de {atividade}."
)

model_prompt.format(dias = numero_dias,
                    criancas = numero_criancas,
                    atividade = atividade)

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.5,
    api_key=os.getenv('OPENAI_API_KEY')
    )

resposta = llm.invoke(model_prompt)
#print(resposta.content)