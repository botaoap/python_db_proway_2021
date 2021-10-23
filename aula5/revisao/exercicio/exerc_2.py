# Crie uma classe de Produtos que tenha nome valor e categoria
# Essa classe devera conter os metodos de getter e setter
# os atributos devem ser privados

class Produto():
    def __init__(self, valor, categoria) -> None:
        self.__valor = valor
        self.__categoria = categoria
    
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

produto = Produto(10.00, "Limpeza")
print(produto.categoria)
print(produto.valor)

# produto.categoria = "Alimento"
# produto.valor = 5.50

# print(produto.categoria)
# print(produto.valor)
