# Crie uma classe de Testes para a classe de Produtos acima 
# Testando os valores passados

import unittest
from unittest.case import TestCase
from exerc_2 import Produto

class TestProduto(TestCase):

    def setUp(self) -> None:
        self.produto = Produto(15.00, "Limpeza")

    def test_crianto_produto(self):
        self.assertIsInstance(self.produto, Produto)
    
    def test_atributos_classe_produto(self):
        self.assertIsInstance(self.produto.categoria, str)
        self.assertIsInstance(self.produto.valor, float)

if __name__ == "__main__":
    unittest.main()
