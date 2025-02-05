import unittest
from robo import *


class TestePerfumes(unittest.TestCase):

    def setUp(self): #inicia o chat
        self.robo = iniciar() #apos isso, armazena na variavel

    #testa se o chat entende diferentes perguntas 
    def testar_nota_olfativa(self):
        mensagens = ["O que significa nota olfativa?", "o que é nota olfativa", "nota olfativa", "quais as notas olfativas", "o que e nota olfativa"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                "Nota olfativa é a classificação dos aromas de um perfume em três estágios: Notas de topo: São as primeiras a serem sentidas, leves e voláteis. Notas de coração: Definem a identidade do perfume, mais equilibradas. Notas de base: Fixam a fragrância, duram mais tempo na pele.", resposta.text
            )
            
    #testa se o chat entende diferentes perguntas         
    def testar_familia_olfativa(self):
        mensagens = ["Quais são as famílias olfativas?", "o que é familia olfativa?", "familia olfativa", "familias olfativas","o que significa familia olfativa?", "o que e familia olfativa?", "Quais sao as famílias olfativas?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                "Família olfativa é um sistema de classificação de perfumes que agrupa fragrâncias com características semelhantes. Os perfumes são classificados em cítricos, florais, orientais, amadeirados, aromáticos, aquáticos, chipres e gourmand, cada um com características próprias.", resposta.text
            )
            
    #testa se o chat entende diferentes perguntas         
    def testar_perfume_arabe(self):
        mensagens = ["Qual o diferencial de um perfume árabe?", " o que é um perfume árabe?", " o que e um perfume arabe?", "perfume arabe", "qual a diferenca de um perfume arabe", "Qual o diferencial de um perfume arabe?", "o que é um perfume árabe", "perfume árabe", "perfumes arabes"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                "Os perfumes árabes se destacam pela alta concentração de óleos essenciais, resultando em fragrâncias intensas, exóticas e duradouras. Eles costumam ter notas amadeiradas, orientais e especiadas, como oud, âmbar, almíscar e açafrão, além de serem frequentemente baseados em ingredientes naturais e sem álcool.Diferente dos ocidentais que possui mais variedade de famílias olfativas, presença de álcool, fragrâncias mais leves e frescas, com menor fixação comparada aos árabes.", resposta.text
            )
            
    #testa se o chat entende diferentes perguntas         
    def testar_primeiro_perfume(self):
        mensagens = ["Quando surgiu o primeiro perfume?", "De quando é o primeiro perfume", "primeiro perfume", "De quando é o primeiro perfume"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                "O primeiro perfume surgiu por volta de 2.000 a.C. na Mesopotâmia e Egito, onde era usado em rituais religiosos e pela nobreza. A primeira perfumista registrada foi Tapputi, uma química mesopotâmica que destilava flores e resinas para criar fragrâncias.", resposta.text
            )
            
    #testa se o chat entende diferentes perguntas         
    def testar_tipos_perfume(self):
        mensagens = ["quais os tipos de perfume?", "tipos de perfume?", "diferenciar os tipos de perfume?", "como diferenciar os tipos de perfume?", "quais são os tipos de perfume?", "quais sao os tipos de perfume?"]

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA) #verifica a confiança
            self.assertIn(
                "Os perfumes são diferenciados principalmente pela concentração de essência na sua composição, o que afeta a intensidade e duração da fragrância na pele. -Parfum: concentração de 20% a 40% de essencia, duração de 8h a 12h e fragrância intensa e marcante. -Eau de Parfum (EDP): concentração de 15% a 20% de essencia, duração 6-10h e frangancia forte. -Eau de Toilette (EDT): concentração de 5% a 15% de essencia, duração de 4h a 8h e fragrância moderada. -Eau de Cologne (EDC): concentração de 2% a 5%, duração de 2h a 4h e fragrancia suave.-Eau Fraîche: concentração <3%, duração de 1h a 3h e fragrancia bem leve e suave.", resposta.text
            )

#roda o teste
if __name__ == "__main__":
    carregador = unittest.TestLoader() #cria um carregador de testes automatico
    testes = unittest.TestSuite() #cria um conjunto vazio onde os testes serão adicionados antes mesmo de serem executados

    testes.addTest(carregador.loadTestsFromTestCase(TestePerfumes)) #busca metodos de teste na TestePerfume

    executor = unittest.TextTestRunner() #cria o executor de testes
    executor.run(testes) #roda os testes e exibe