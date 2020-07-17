from graphviz import Digraph


class TransicaoNegada(Exception):
    pass


class PedidoEstadoInterface(object):
    """
    Classe básica abstrata do estado de um pedido
    """

    def criar_pedido(self):
        raise TransicaoNegada("Transição negada: Criar Pedido")

    def novo_produto(self):
        raise TransicaoNegada("Transição negada: Novo Produto")

    def pagamento_pendente(self):
        raise TransicaoNegada("Transição negada: Pagamento Pendente")

    def pedido_aprovado(self):
        raise TransicaoNegada("Transição negada: Pedido Aprovado")

    def em_transporte(self):
        raise TransicaoNegada("Transição negada: Em Transporte")

    def entregue(self):
        raise TransicaoNegada("Transição negada: Entregue")

    def entrega_finalizada(self):
        raise TransicaoNegada("Transição negada: Entrega Finalizada")

    def pedido_cancelado(self):
        raise TransicaoNegada("Transição negada: Pedido Cancelado")

    def extraviado(self):
        raise TransicaoNegada("Transição negada: Extraviado")

    def __str__(self):
        return self.nome if hasattr(self, 'nome') else self.__class__.__name__


class FazerPedido(PedidoEstadoInterface):
    nome = 'Fazer Pedido'

    def novo_produto(self):
        return NovoProduto()

    def pedido_cancelado(self):
        return PedidoCancelado()


class NovoProduto(PedidoEstadoInterface):
    nome = "Novo Produto"

    def pagamento_pendente(self):
        return PagamentoPendente()

    def pedido_cancelado(self):
        return PedidoCancelado()


class PagamentoPendente(PedidoEstadoInterface):
    nome = "Pagamento Pendente"

    def pedido_aprovado(self):
        return PedidoAprovado()

    def pedido_cancelado(self):
        return PedidoCancelado()


class PedidoAprovado(PedidoEstadoInterface):
    nome = 'Aprovado'

    def em_transporte(self):
        return EmTransporte()

    def pedido_cancelado(self):
        return PedidoCancelado()


class EmTransporte(PedidoEstadoInterface):
    nome = "Em Transporte"

    def entregue(self):
        return Entregue()

    def pedido_cancelado(self):
        return PedidoCancelado()


class Entregue(PedidoEstadoInterface):
    nome = "Entregue"

    def extraviado(self):
        return Extraviado()

    def entrega_finalizada(self):
        return EntregaFinalizada()


class PedidoCancelado(PedidoEstadoInterface):
    nome = 'Cancelado'


class EntregaFinalizada(PedidoEstadoInterface):
    nome = "Finalizado"


class Extraviado(PedidoEstadoInterface):
    nome = "Extraviado"


class Pedido(object):

    def __init__(self, estado):
        self.estado = estado

    def mudar(self, novo_estado):
        if isinstance(novo_estado, PedidoEstadoInterface):
            self.estado = novo_estado
            print("Estado:", self.pegar_estado())
        else:
            raise ValueError

    def pegar_estado(self):
        return self.estado

    def criar_pedido(self):
        self.mudar(self.estado.novo_produto())

    def adicionar_produto(self):
        self.mudar(self.estado.novo_produto())

    def set_pagamento_pendente(self):
        self.mudar(self.estado.pagamento_pendente())

    def set_pedido_aprovado(self):
        self.mudar(self.estado.pedido_aprovado())

    def set_em_transporte(self):
        self.mudar(self.estado.em_transporte())

    def set_entregue(self):
        self.mudar(self.estado.entregue())

    def set_entrega_finalizada(self):
        self.mudar(self.estado.entrega_finalizada())

    def set_pedido_cancelado(self):
        self.mudar(self.estado.pedido_cancelado())

    def set_extraviado(self):
        self.mudar(self.estado.extraviado())


if __name__ == "__main__":
    produto = Pedido(NovoProduto())

    try:
        # produto.set_pedido_cancelado()
        # produto.adicionar_produto()
        # produto.set_pedido_cancelado()
        produto.set_pagamento_pendente()
        # produto.set_pedido_cancelado()
        produto.set_pedido_aprovado()
        # produto.set_pedido_cancelado()
        produto.set_em_transporte()
        # produto.set_pedido_cancelado()
        produto.set_entregue()
        produto.set_entrega_finalizada()
        produto.set_extraviado()
    except TransicaoNegada as err:
        print(f"Não é possível mudar para o estado pois -> {str(err)}, a partir do estado {produto.pegar_estado()}")

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
