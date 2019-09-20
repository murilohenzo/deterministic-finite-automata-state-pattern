from graphviz import Digraph

class PedidoEstado(object):
    "Classe básica abstrata do estado de um pedido"

    nome = "estado"
    permitido = []

    def transicao(self, estado):
        if estado.nome in self.permitido:
            print(f"Estado [{self}] ==> alternado para novo estado de [{estado.nome}]")
            self.__class__ = estado
        else:
            print(f"Estado {self} ==> alternado para {estado.nome} negado")

    def __str__(self):
        return self.nome

class FazerPedido(PedidoEstado):
    nome = 'Fazer Pedido'
    permitido = ['Novo Produto', 'Cancelado']

class NovoProduto(PedidoEstado):
    nome = "Novo Produto"
    permitido = ['Pagamento Pendente' ,'Cancelado']

class PagamentoPendente(PedidoEstado):
    nome = "Pagamento Pendente"
    permitido = ['Aprovado', 'Cancelado']

class PedidoAprovado(PedidoEstado):
    nome = 'Aprovado'
    permitido = ['Em Transporte', 'Cancelado']

class EmTransporte(PedidoEstado):
    nome = "Em Transporte"
    permitido = ['Entregue', 'Cancelado']

class Entregue(PedidoEstado):
    nome = "Entregue"
    permitido = ['Extraviado', 'Finalizado']

class ProdutoCancelado(PedidoEstado):
    nome = 'Cancelado'
    permitido = None

class EntreguaFinalizada(PedidoEstado):
    nome = "Finalizado"
    permitido = None

class Extravido(PedidoEstado):
    nome = "Extraviado"
    permitido = None

class Produto(object):

    def __init__(self, modelo = 'PS4'):
        self.modelo = modelo
        self.estado = FazerPedido()

    def mudar(self, estado):
        self.estado.transicao(estado)

if __name__ == "__main__":
    produto = Produto()
    #produto.mudar(ProdutoCancelado)
    produto.mudar(NovoProduto)
    #produto.mudar(ProdutoCancelado)
    produto.mudar(PagamentoPendente)
    #produto.mudar(ProdutoCancelado)
    produto.mudar(PedidoAprovado)
    #produto.mudar(ProdutoCancelado)
    produto.mudar(EmTransporte)
    #produto.mudar(ProdutoCancelado)
    produto.mudar(Entregue)
    produto.mudar(EntreguaFinalizada)
    #produto.mudar(Extravido)

    f = Digraph('Automato Finito Deterministico')
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    f.node('Cancelado')
    f.node('Finalizado')
    f.node('Extraviado')

    f.attr('node', shape='circle')
    f.edge('Fazer Pedido', 'Novo Produto', label='1')
    f.edge('Fazer Pedido', 'Cancelado', label='0')
    f.edge('Novo Produto', 'Pagamento Pendente', label='1')
    f.edge('Novo Produto', 'Cancelado', label='0')
    f.edge('Pagamento Pendente', 'Cancelado', label='0')
    f.edge('Pagamento Pendente', 'Aprovado', label='1')
    f.edge('Aprovado', 'Cancelado', label='0')
    f.edge('Aprovado', 'Em Transporte', label='1')
    f.edge('Em Transporte', 'Cancelado', label='0')
    f.edge('Em Transporte', 'Entregue', label='1')
    f.edge('Entregue', 'Extraviado', label='0')
    f.edge('Entregue', 'Finalizado', label='1')

    f.view()