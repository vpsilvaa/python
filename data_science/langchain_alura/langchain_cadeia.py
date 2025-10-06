from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequencialChain
from langchain.globals import set_debug
from dotenv import load_dotenv
import warnings
import os

load_dotenv()
set_debug(True)

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.5,
    api_key=os.getenv('OPENAI_API_KEY')
    )

model_cidade = ChatPromptTemplate.from_template(
    'Sugira uma cidade dado meu interesse por {interesse}'
)

model_restaurante = ChatPromptTemplate.from_template(
    'Sugira restaurantes populares entre locais em {cidade}'
)

model_cultural = ChatPromptTemplate.from_template(
    'Sugira atividade e locais culturais em {cidade}'
)

cadeia_cidade = LLMChain(prompt=model_cidade, llm=llm)
cadeia_restaurantes = LLMChain(prompt=model_cidade, llm=llm)
cadeia_cultural = LLMChain(prompt=model_cidade, llm=llm)

cadeia = SimpleSequencialChain(chains=[cadeia_cidade, cadeia_restaurantes, cadeia_cultural])

resultado = cadeia.invoke('praias')
print(resultado)