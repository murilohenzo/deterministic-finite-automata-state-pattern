from DFA.dfa import AutomatoFinitoDeterministico


p1 = AutomatoFinitoDeterministico(3).criarAutomato()

# editar estados de transicao do automato criado 
p1['Q0'][0] = 'Q0'
p1['Q0'][1] = 'Q1'
p1['Q1'][0] = 'Q2'
p1['Q1'][1] = 'Q0'
p1['Q2'][0] = 'Q1'
p1['Q2'][1] = 'Q2'

print(AutomatoFinitoDeterministico.validarLinguagem(p1, 'Q0', {'Q0'}, '1011101'))
