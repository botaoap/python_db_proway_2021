# Static Class
import uuid
class GeradorDeId:

    @staticmethod
    def gerar_id():
        return uuid.uuid4()

print(GeradorDeId().gerar_id())
print(GeradorDeId.gerar_id())

# o staticmethod nao conhece nada sobre a classe, nao pod eacessar nenhum valor

class MinhaClasse:

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def metodo_estatico():
        # ele nao tem acesso aos atributos
        # nao vai acahr o valor de self.nome
        print("Eu sou um metodo estatico")