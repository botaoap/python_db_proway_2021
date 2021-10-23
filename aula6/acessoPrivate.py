class Pessoa:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__idade = 24

pessoa = Pessoa("Botão")

# Acessar atributos privados de fora da classe
print(pessoa._Pessoa__nome)
print(pessoa._Pessoa__idade)
