# Teste os seguintes retornos da classe abaixo
#
import unittest
from unittest import TestCase

class ClasseDeTreino:

    def retornando_uma_lista(self):
        return []
    
    def retornando_uma_tupla(self):
        return ()
    
    def retornando_um_dicionario(self):
        return {}
    
    def retornando_uma_string(self):
        return "String"
    
    def retornando_um_integer(self):
        return 1

    def retornando_um_float(self):
        return 1.1
    
    def retornando_um_boolean(self):
        return True

class TestTreino(TestCase):

    def test_return_list(self):
        self.assertEqual(ClasseDeTreino().retornando_uma_lista(), [])

    def test_return_tuple(self):
        self.assertEqual(ClasseDeTreino().retornando_uma_tupla(), ())
    
    def test_return_dictionary(self):
        self.assertEqual(ClasseDeTreino().retornando_um_dicionario(), {})

    def test_return_string(self):        
        self.assertIsInstance(ClasseDeTreino().retornando_uma_string(), str)
    
    def test_return_int(self):
        self.assertIsInstance(ClasseDeTreino().retornando_um_integer(), int)
    
    def test_return_float(self):
        self.assertIsInstance(ClasseDeTreino().retornando_um_float(), float)
    
    def test_return_boolean(self):
        self.assertIsInstance(ClasseDeTreino().retornando_um_boolean(), bool)

if __name__ == "__main__":
    unittest.main()
