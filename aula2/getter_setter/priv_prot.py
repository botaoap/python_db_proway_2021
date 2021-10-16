'''
_ protected
__ private
'''

_a = "Protected"
__a = "Private"

class Produto:

    def __init__(self, nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor
    
    # Getter
    def ler_nome(self):
        return self.__nome
    
    # Getter
    def ler_valor(self):
        return self.__valor
    
    # Setter
    def configurar_nome(self, nome):
        self.__nome= nome

    # Setter
    def configurar_valor(self, valor):
        self.__valor = valor

    def _falar_algo(self):
        print("Falei alguma coisa")

    def __falei_um_segredo(self):
        print("N sera possivel ver isso de fora")

produto = Produto("Refrigerante", 5.80)

print(produto.ler_nome())
print(produto.ler_valor())

produto.configurar_nome("Agua")
produto.configurar_valor(3)

print(produto.ler_nome())
print(produto.ler_valor())

produto._falar_algo()
produto.__falei_um_segredo()