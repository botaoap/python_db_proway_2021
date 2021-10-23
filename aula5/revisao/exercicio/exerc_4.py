# Crie uma classe de produto e uma classe que de categoria
# Essa  classe de cateogria devera ser passada para um metodo
# de registro de produto da classe Produto
# Exemplo
# >>>> produto = Produto()
# >>>> categoria = Categoria("Limpeza")
#
# >>>> produto.registrar_produto("Sabao em pó", 17.50, categoria)
# >>>> print(produto.banco_de_dados)
# >>>> {nome: "Sabao em pó", preço: 17.50, categoria: Categoria}

class Produto():
    def __init__(self) -> None:
        self.registar_produto(self.__nome,self.__valor,self.__categoria)
        self.banco_de_dados = []
    
    def registar_produto(self, nome, valor, categoria):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        
    
    @property
    def nome(self):
        return self.__nome

    @valor.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

class Categria():
    
    def __init__(self, nome) -> None:
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome

    @valor.setter
    def nome(self, valor):
        self.__nome = valor

