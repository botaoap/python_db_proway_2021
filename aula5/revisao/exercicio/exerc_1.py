# Crie um metodo que receba por input o nome idade e sexo
# esse metoddo deve printar na tela uma string formatada
# Exemplo "MEu nome é Joao e tenho 47 anos de idade"

class Pessoa:
    def __init__(self, nome, idade, sexo) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        self.__idade = valor
    
    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, valor):
        self.__sexo = valor
    
    def show_who_i_am(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos de idade"

pessoa = Pessoa("Heloise", 19, "F'")
print(pessoa.show_who_i_am())