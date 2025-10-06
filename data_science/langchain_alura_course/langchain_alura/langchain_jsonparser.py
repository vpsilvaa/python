from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequencialChain
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from langchain.globals import set_debug
from dotenv import load_dotenv
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

cadeia_cidade = LLMChain(prompt=modelo_cidade, llm=llm)
cadeia_restaurantes = LLMChain(prompt=modelo_restaurantes, llm=llm)
cadeia_cultural = LLMChain(prompt=modelo_cultural, llm=llm)

cadeia = SimpleSequentialChain(chains=[cadeia_cidade, cadeia_restaurantes, 
                                       cadeia_cultural
                                       ],
                                verbose=True)

resultado = cadeia.invoke("praias")
print(resultado)

# -----------------------------------------------------------------------------

# from langchain.output_parsers import DatetimeOutputParser
# from langchain.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     temperature=0.5,
#     api_key=os.getenv("OPENAI_API_KEY"))

# parseador_saida = DatetimeOutputParser()
# modelo_data = """Responda a pergunta do usuário: 
#     {pergunta}

#     {formato_saida}
# """

# prompt = PromptTemplate.from_template(
#     modelo_data,
#     partial_variables={"formato_saida": parseador_saida.get_format_instructions()},
# )

# PromptTemplate(
#     input_variables=['question'], 
#     partial_variables={'formato_saida': "Write a datetime string that matches the following pattern: '%Y-%m-%dT%H:%M:%S.%fZ'.\n\nExamples: 0668-08-09T12:56:32.732651Z, 1213-06-23T21:01:36.868629Z, 0713-07-06T18:19:02.257488Z\n\nReturn ONLY this string, no other words!"}, template='Answer the users question:\n\n{question}\n\n{format_instructions}')

# chain = prompt | llm | parseador_saida

# resposta = chain.invoke({"pergunta": "Quando a bitcoin foi fundada?"})

# print(resposta)