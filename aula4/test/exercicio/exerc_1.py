# Crie testes usando as seguintes condicoes
# not - and - or - == - !=
# Not - Verifica se o valor nao é verdadeiro
# And - Verifica se as duas condicoes sao verdadeiras
# OR - Verifica se uma das condicoes sao verdadeiras
# == - Veridica igualdade entre dois valores
# != - Verifica se os valores sao diferentes

from datetime import date
from unittest import TestCase
import unittest

class Test(TestCase):

    def test_with_not(self):
        a = "    "
        a = a.strip()

        assert not a
    
    def test_with_and(self):
        pessoa1 = "Jorge"
        pessoa2 = "Maria"
        pessoa3 = "Gabriel"
        pessoa4 = "Heloise"

        assert pessoa1 != pessoa2 and pessoa3 != pessoa4
    
    def test_with_or(self):
        numero1 = 1
        numero2 = 2
        numero3 = '3'

        assert type(numero1) == type(numero2) or type(numero1) != type(numero3)
    
    def test_startwith(self):
        name = "Maria"

        assert name.startswith("M")
        assert name.endswith("a")
    
    def test_with_diff(self):
        n1 = 5
        n2 = 10
        
        assert n1 != n2
    
    def test_with_equal(self):
        ano1 = 2021
        ano2 = date.today().year

        assert ano1 == ano2
    
if __name__ == "__main__":
    unittest.main()