# Crie uma classe de Produtos
# Que tenha seus atributos preivados __
# utilizando o getter e setter para poder alterar seus valores
# Sem property 

# Crie uma classe de Categorias
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Com property

class Produto:

    def __init__(self, nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor
    
print("Usando getter setter padrao")
produto = Produto(nome="Agua", valor=5.00)
print(produto.get_nome())
print(produto.get_valor())

produto.set_nome("Refigerante")
produto.set_valor(11.00)

print(produto.get_nome())
print(produto.get_valor())
print()

class Categoria:

    def __init__(self, nome) -> None:
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

print("Usando getter e setter com property")
caregoria = Categoria(nome="Bebidas")
print(caregoria.nome)

caregoria.nome = "Comidas"

print(caregoria.nome)
