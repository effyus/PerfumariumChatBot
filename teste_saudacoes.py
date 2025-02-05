import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self): #inicia o chat
        self.robo = iniciar() #apos isso, armazena na variavel
    
    #testa se o chat entende diferentes perguntas    
    def testar_oi_ola(self):
        saudacoes = [ "oi", "olá", "tudo bem?", "como vai?", "ola" ]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                "Olá, sou o perfumarium, qual a sua duvida?", 
                resposta.text
            )
            
    #testa se o chat entende diferentes perguntas
    def testar_bom_dia_boa_tarde_boa_noite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                saudacao + ", sou o perfumarium, qual a sua duvida?",
                resposta.text
            )

    #testa se o chat entende diferentes perguntas
    def testar_variabilidades_saudacoes(self):
        saudacoes = [ "Bom dia", "Boa tarde", "Boa noite" ]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response("oi, " + saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                saudacao + ", sou o perfumarium, qual a sua duvida?",
                resposta.text
            )


#roda o teste
if __name__ == "__main__":
    carregador = unittest.TestLoader() #cria um carregador de testes automatico
    testes = unittest.TestSuite() #cria um conjunto vazio onde os testes serão adicionados antes mesmo de serem executados

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes)) #busca metodos de teste na TestePerfume

    executor = unittest.TextTestRunner() #cria o executor de testes
    executor.run(testes) #roda os testes e exibe