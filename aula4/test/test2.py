import unittest
import re

# class TestModel(unittest.TestCase):

#     def test_alguma_coisa(self):
#         self.assertEqual(1,1)
    
#     def test_assert_false(self):
#         a = " "
#         a = a.strip()

#         self.assertFalse(a)

#     def test_instance(self):
#         self.assertIsInstance(1, int)


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Pessoa:

    def __init__(self, nome, idade, email) -> None:
        self.nome = self.valida_nome(nome)
        self.idade = self.valida_idade(idade)
        self.email = self.valida_email(email)
    
    def valida_nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError
        return nome
    
    def valida_idade(self, idade):
        if not isinstance(idade, int):
            raise ValueError
        return idade

    def valida_email(self, email):
        if(re.fullmatch(regex, email)):
           return email
        else:
            raise ValueError

class TestPessoa(unittest.TestCase):

    def test_criar_pessoa(self):
        pessoa = Pessoa("Marley", 25, "email_da_pessoa@proway.com")

        self.assertIsInstance(pessoa, Pessoa)
    
    def test_pessoa_com_valor_correto_nos_atributos(self):
        pessoa = Pessoa("A", 25, "email_da_pessoa@proway.com")

        self.assertIsInstance(pessoa.nome, str)
        self.assertIsInstance(pessoa.idade, int)
        self.assertIsInstance(pessoa.email, str)

    def test_valores_esperados(self):
        # Preparação do teste
        nome = "Marley"
        idade = 25
        email = "email_da_pessoa@proway.com"

        # Ação ou Execução do teste
        pessoa = Pessoa(nome, idade, email)

        # Asserção
        self.assertEqual(pessoa.nome, nome)
        self.assertEqual(pessoa.idade, idade)
        self.assertEqual(pessoa.email, email)

if __name__ == "__main__":
    unittest.main()