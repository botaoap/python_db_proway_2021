# Crie uma classe de produtos com classmethod
# Que valide se o valor do produto passado é um float
# A classe podera aceitar esse valor R$15.00
# Que devera ser transformada para um float

# nome = "CASCATA"
# nome.replace("A","@")

# produto = Produto.cria_classe("R$15,00")
# print(produto.valor)

"""
Saida no terminal
>>>> 15.00
"""

class Produto:

    def __init__(self, preco_prod) -> None:
        self.preco_prod = preco_prod

    @classmethod
    def cria_classe(cls, preco_prod):
        replace_price = preco_prod.replace("R$", "")
        return cls(float(replace_price))

produto = Produto.cria_classe("R$15.00")
print(format(produto.preco_prod, '.2f'))

total = produto.preco_prod + 2.5
print(format(total, '.2f'))