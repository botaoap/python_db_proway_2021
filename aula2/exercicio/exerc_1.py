# Crie uma classe que contenha um classmethod
# Que devera criar pelo ano de nascimento
# e validar se a idade é maior que 18

class Pessoa:

    def __init__(self, nome, ano_nasc) -> None:
        self.nome = nome
        self.ano_nasc = ano_nasc
    
    @classmethod
    def verifica_idade(cls, nome, ano_nasc):
        validar = 2021 - ano_nasc
        if (validar < 18):
            raise Exception("Proibido menor que 18 anos")
        return cls(nome, ano_nasc)
    
validacao = Pessoa.verifica_idade("Jorge", 1999)
print(validacao.ano_nasc)