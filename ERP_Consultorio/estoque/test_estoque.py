import unittest
from estoque.estoque import Estoque
from estoque.fornecedor import Fornecedor
#from estoque import Estoque, Fornecedor
#from estoque.fornecedor import Fornecedor

class TestEstoque(unittest.TestCase):
    def setUp(self):
        # Inicializa os objetos de teste
        self.estoque = Estoque(1, "Cimento", "Fornecedor A", "Cimento odontológico")
        self.fornecedor = Fornecedor(1, "Fornecedor A", "123456789", "fornecedor@a.com")

    def test_adicionar_produto(self):
        # Verifica se o produto foi adicionado corretamente ao estoque
        self.estoque.adicionar_produto(self.fornecedor, "Cimento", 100)
        self.assertIn("Cimento", self.estoque.consultar_produtos())

    def test_consultar_produtos(self):
        # Verifica se os produtos podem ser consultados corretamente
        self.estoque.adicionar_produto(self.fornecedor, "Cimento", 100)
        produtos = self.estoque.consultar_produtos()
        self.assertEqual(len(produtos), 1)
        self.assertEqual(produtos[0], "Cimento")

    def test_montar_carrinho(self):
        # Adicionando produtos ao estoque
        self.estoque.adicionar_produto(self.fornecedor, "Cimento", 100)
        self.estoque.adicionar_produto(self.fornecedor, "Resina", 50)
        self.estoque.adicionar_produto(self.fornecedor, "Luva", 200)

        # Criando o carrinho com alguns itens
        carrinho = self.estoque.montarCarrinho(["Cimento", "Luva"])

        # Verificando se o carrinho contém os itens certos
        self.assertEqual(len(carrinho), 2)
        self.assertEqual(carrinho[0]['produto'], "Cimento")
        self.assertEqual(carrinho[1]['produto'], "Luva")

if __name__ == '__main__':
    unittest.main()
