from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import json

CONVERSAS = [
    "conversas/saudacoes.json",
    "conversas/infos_perfume.json"
]

# cria um chat e retorna o treinador (Listtrainer)
def configurar():
    time.clock = time.time

    robo = ChatBot("CHATBOT PERFUMARIUM")
    treinador = ListTrainer(robo)

    return True, treinador


# carrega as conversas do json
def carregar_conversas():
    carregadas, conversas = True, [] #verifica os dados

    for arquivo_de_conversas in CONVERSAS:
        try:
            with open(arquivo_de_conversas, "r", encoding="utf-8") as arquivo:
                para_treinar = json.load(arquivo)
                conversas.append(para_treinar["conversas"]) #armazena as conversas

                arquivo.close()
        except Exception as e:
            carregadas = False #caso ocarra um erro, sera dado como falha no carregamento

    return carregadas, conversas

# recebe o treinador e as conversas carregadas
def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            print(f"\nTreinando chatbot PERFUMARIUM\nmensagens: {mensagens},\nresposta: {resposta}")
            for mensagem in mensagens: # Treina o bot para reconhecer cada variação da pergunta
                treinador.train([mensagem, resposta]) 

#execucao do codigo
if __name__ == "__main__":
    configurado, treinador = configurar() #configurar o chat

#verifica a configuração, carrega e depois treina
    if configurado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinar(treinador, conversas)