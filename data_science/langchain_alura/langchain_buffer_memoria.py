from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.globals import set_debug
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
import os
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()
set_debug(True)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY"))

mensagens = [
        "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
        "Qual é o melhor período do ano para visitar em termos de clima?",
        "Quais tipos de atividades ao ar livre estão disponíveis?",
        "Alguma sugestão de acomodação eco-friendly por lá?",
        "Cite outras 20 cidades com características semelhantes as que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
        "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]


memory = ConversationBufferMemory()
#memory = ConversationBufferWindowMemory(k=2)
#memory = ConversationSummaryMemory(llm=llm)

conversation = ConversationChain(llm=llm,
                                 verbose=True,
                                 memory=memory)

for mensagem in mensagens:
    resposta = conversation.predict(input=mensagem)
    print(resposta)

print(memory.load_memory_variables({}))
