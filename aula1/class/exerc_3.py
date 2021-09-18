# Crie uma classe que escreva em um arquivo
# Crie um classe que crie um produto para registrar dentro do arquivo
# Criterios:
# Os Produtos devem conter:
#   -id(integer)
#   -nome(string)
#   -preço(float)

# Cadastre ao menos 5 produtos e faça com que sejam impressos no terminal
# Exemplo de saida

"""
{'id': 1, 'nome': 'cocla-cola', 'preco': 7.79}

{'id': 2, 'nome': 'pepsi', 'preco': 7.79}

{'id': 3, 'nome': 'fanta', 'preco': 7.79}

{'id': 4, 'nome': 'guarana', 'preco': 7.79}

{'id': 5, 'nome': 'sprite', 'preco': 7.79}
"""

# open("abacaxi.txt", "w") escreve no arquivos
# open("abacaxi.txt", "a") adociona no arquivos
# open("abacaxi.txt", "r") le o arquivos

with open("aula1/abacaxi.txt", "w") as arquivo:
    arquivo.write("Escrevendo dentro do arquivo")

class Produto:

    def __init__(self,id):
        self.id = id
        self.nome = input("Nome do produto: ")
        self.preco = input("Preço do produto: ")
        self.file_name = ""
        self.option = ""

    def create_file(self, body):
        with open(f"aula1/arq_exerc_3.txt", "a") as file:
            file.write(f"{body} \n")

    def cadastrar(self):
        dict_product = {
                    'id': self.id,
                    'nome': self.nome,
                    'preco': self.preco
                }
        self.create_file(dict_product)
        
import os

quest = int(input("Quantos produtos cadastrar? "))
# file_name = input("Escolha o nome do arquivo: ")
count = 0

for quest in range(quest):
    count += 1
    Produto(id= count).cadastrar()
    os.system('clear') or None