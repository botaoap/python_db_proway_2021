"""
classmethod - staticmethod - dcorators
"""
class MinhaClasse:

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def __repr__(self) -> str:
        return f"{self.nome}, {self.idade}"

    def metodo_de_instancia(self):
        print(f"Eu sou uma classe {self}")
        print(f"Meu nome é {self.nome}")
    # classmethod normalmente usado para cirar classes apartir dele
    # o classmethod conhece o que existe dentro da class
    # podendo alterar os valores da classe por exemplo o __init__ 
    @classmethod
    def metodo_de_classe(cls, nome, idade):
        if idade < 18:
            raise Exception("Nao pode menor de idade")
        return cls(nome, idade)

minha_classe = MinhaClasse(nome="Jorge", idade=25)
# print(minha_classe.nome)
# print(minha_classe.idade)
print(minha_classe)

outra_classe = MinhaClasse.metodo_de_classe("Junior", 19)
print(outra_classe.idade)