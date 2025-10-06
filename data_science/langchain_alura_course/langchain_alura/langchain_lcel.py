from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequencialChain
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain.globals import set_debug
from dotenv import load_dotenv
from operator import itemgetter
import warnings
import os

load_dotenv()
set_debug(True)

class Destino(BaseModel):
    cidade = Field('cidade a visitar')
    motivo = Field('motivo pelo qual é interessante visitar a cidade')

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.5,
    api_key=os.getenv('OPENAI_API_KEY')
    )

parseador = JsonOutputParser(pydantic_object=Destino)

model_cidade = PromptTemplate(
    template = """Sugira uma cidade dado meu interesse por {interesse},
    {formatacao_de_saida}
    """,
    input_variables=['interesse'],
    partial_variables={'formatacao_de_saida': parseador.get_format_instructions()},
)

model_restaurante = ChatPromptTemplate.from_template(
    'Sugira restaurantes populares entre locais em {cidade}'
)

model_cultural = ChatPromptTemplate.from_template(
    'Sugira atividade e locais culturais em {cidade}'
)

model_final = ChatPromptTemplate.from_messages(
    [
    ('ai', 'Sugestão de viagem para a cidade: {cidade}.\n'),
    ('ai', 'Motivo: {motivo}.\n'),
    ('ai', 'Restaurantes populares: {model_restaurantes}.\n'),
    ('ai', 'Locais culturais: {locais_culturais}.\n'),
     ('system', 'Combine todas as informações acima em uma resposta final completa de 2 parágrafos')
    ]
)

parte1 = model_cidade | llm | parseador
parte2 = model_restaurante | llm | StrOutputParser()
parte3 = model_cultural | llm | StrOutputParser()
parte4 = model_final | llm | StrOutputParser()

cadeia = (parte1 | {'model_restaurantes': parte2, 
                    'locais_culturais': parte3,
                    'cidade': itemgetter('cidade')} 
                    | parte4) 

resultado = cadeia.invoke({'interesse': 'praias'})
print(resultado)
