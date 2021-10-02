# Crie uma classe que possa cadastrar Produtos
# fazendo o uso dos modelos getters e setters
# Essa classe deve conter validacoes dos valores recebidos
# nao podendo enviar letras por exemplo
# Deve conter cabecalho
# Deve poder cadastrar os valores com metodo input
# Deve ter um menu de escolhas
# Por exemplo

# 1. Cadastrar
# 2. Ler todos
# 3. Ler especifico
# 4. Apagar

"""
------- Bem Vindo -------

# 1. Cadastrar
# 2. Ler todos
# 3. Ler especifico
# 4. Apagar

Digite um numero: 1


-------  Menu de Cadastro ------

digite um nome:
digite um valor:
digite uma categoria:


"""

class Menu:

    def bem_vindo():
        return """
            1. Cadastrar
            2. Ler todos
            3. Ler especifico
            4. Apagar
            5. Sair
            """

class Produto:

    def __init__(self, nome="", valor=0, categoria="") -> None:
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_valor(self):
        return self.valor
    
    def set_valor(self, valor):
        self.valor = valor
    
    def get_categorua(self):
        return self.categoria
    
    def set_categoria(self, categoria):
        self.categoria = categoria

class DbProdutos(Produto):

    list_db = []

    def insert(self):
        self.list_db.append([self.nome, self.valor, self.categoria])

    def update(self, posicao, nome, valor, categoria):
        self.list_db[posicao] = [nome, valor, categoria]
    
    def delete_all(self):
        self.list_db.clear()

    def delete_one(self, posicao):
        self.list_db.pop(posicao)

    def search_all(self):
        return print(self.list_db)

    def search_one(self, posicao):
        return print(self.list_db[posicao])
    
while (True):
    print(Menu.bem_vindo())
    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):
        nome = input("Nome do produto: ")
        valor = input("Valor do produto: ")
        categoria = input("Categoria do produto: ")
        lista = DbProdutos(nome= nome, valor= valor, categoria= categoria)
        lista.insert()
    elif (opcao == 2):
        lista.search_all()
    elif (opcao == 3):
        print("Pesquise atraves de uma posicao")
        posicao = int(input("Escolha uma posicao: "))
        lista.search_one(posicao=posicao)
    elif (opcao == 4):
        print("Delete atraves de uma posicao")
        posicao = int(input("Escolha uma posicao: "))
        lista.delete_one(posicao=posicao)
    elif (opcao == 5):
        print("Saiu do sistema!!")
        break