from flask import Flask, jsonify
from robo import *

#cria m app flask
servico = Flask("PERFUMARIUM")

#inicia o chatbot
configurado, robo = configurar()

# a rota retorna infos sobre o chatbot
@servico.route("/perfume/info", methods=["GET"])
def get_informacoes():
    return jsonify(
        nome = "PERFUMARIUM",
        descricao = "O robo do mundo da perfumaria",
        email = "fernansouzadev@gmail.com",
        versao = "1.0",
        robo_online = configurado
    )

#retorna a resposta com base na mensagem de pergunta
@servico.route("/perfume/resposta/<string:mensagem>", methods=["GET"])
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem) #processa a mensagem

    return jsonify(
        resposta = resposta.text,
        confianca = resposta.confidence,
    )


if __name__ == "__main__":
    servico.run(debug=True) #inicia o flask e ativa o modo de depuração