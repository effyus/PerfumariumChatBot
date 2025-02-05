from chatterbot import ChatBot
import time
time.clock = time.time

CONFIANCA_MINIMA = 0.55

# Configura e cria o chatbot
def configurar():
    robo = ChatBot("CHATBOT PERFUMARIUM", read_only = True, logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}]) #bestMatch escolhe a melhor resposta
    
    return True, robo

#Executa o bot atraves de um loop infinito de coleta de mensagens
def executar(robo):
    while True:
        mensagem = input("\nCHATBOT PERFUMARIUM \nDigite sua duvida?\nUsuário >> ")
        resposta = robo.get_response(mensagem.lower()) #obtem as respostas e converte para letras maiusculas
        if resposta.confidence >= CONFIANCA_MINIMA: #testa a confiança
            print(f"\nPERFUMARIUM >> {resposta.text} [confiança={resposta.confidence}]")
        else:
            print(f"Não entendi a sua pergunta [confiança={resposta.confidence}, resposta={resposta.text}]")
            print("Digite novamente")
            
#utiliza essa funçao nos testes, para validação de respostas
def iniciar():
    robo = ChatBot("ChatBot Perfumarium",
                   read_only=True,
                # não aprende novas respostas durante as conversas     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       } #escolhe a melhor resposta
                   ])

    return robo

#execucao do programa
if __name__ == "__main__": 
    configurado, robo = configurar() #cria o chat

    if configurado:
        executar(robo) #executa após a criação