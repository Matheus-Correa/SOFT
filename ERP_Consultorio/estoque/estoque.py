class Estoque:
    def __init__(self, id, produto, fornecedor, descricao):
        self.id = id
        self.produto = produto
        self.fornecedor = fornecedor
        self.descricao = descricao
        self.produtos = []

    def adicionar_produto(self, fornecedor, produto, quantidade):
        self.produtos.append({
            'fornecedor': fornecedor,
            'produto': produto,
            'quantidade': quantidade
        })

    def consultar_produtos(self):
        return [produto['produto'] for produto in self.produtos]

    def montarCarrinho(self, itens):
        """Recebe uma lista de itens e retorna os produtos disponíveis no estoque."""
        carrinho = [produto for produto in self.produtos if produto['produto'] in itens]
        return carrinho

