from itertools import chain


class AutomatoFinitoDeterministico:

    def __init__(self, quantidadeDeEstados):
        self.dfa = {}
        self.quantidadeDeEstados = quantidadeDeEstados

    def criarAutomato(self):
        for estado in range(self.quantidadeDeEstados):
            self.dfa['Q' + str(estado)] = {}
            for transicao in range(2):
                self.dfa['Q' + str(estado)][transicao] = 'Q' + str(transicao)
        return self.dfa

    def validarLinguagem(estadosDeTransicao, estadoInicial, conjuntoDeAceitacao, linguagemDeEntrada):
        estadoAtual = estadoInicial
        keys = set(chain.from_iterable(i.keys() for i in estadosDeTransicao.values()))
        conjuntoBooleano = [int(caractere) in keys for caractere in linguagemDeEntrada]
        for caractere in conjuntoBooleano:
           if caractere != True:
              estadoAtual = None
              return estadoAtual in conjuntoDeAceitacao
           else:
               estadoAtual = estadosDeTransicao[estadoAtual][int(caractere)]
        return estadoAtual not in conjuntoDeAceitacao
