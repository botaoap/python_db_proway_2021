class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade
    # Getter
    @property
    def nome(self):
        return self.__nome
    # Setter
    @nome.setter
    def nome(self, valor: str):
        self.__nome = valor
    
    # Getter
    @property
    def idade(self):
        return self.__idade
    # Setter
    @idade.setter
    def idade(self, valor: int):
        self.__idade = valor

pessoa = Pessoa("Heloise", 19)
print(f'''
Nome: {pessoa.nome}
Idade: {pessoa.idade}
''')


