class Pessoa:
    pass

# Instanciando a classe criada
classe = Pessoa()

# Podemos atribuir qualquer valor pra essas classes
ana = Pessoa()
paulo = Pessoa()
abacaxi = Pessoa()

# Atributos e funcoes dentro de uma classe
class Pessoa:
    
    def falar(self):
        print("Pessoa falando")
    
# Chamando a funcao da classe
# -- Pessoa().falar()

# Passando parametros na funcao
# def falar_algo(assunto):
#     print(f"Este assunto é sobre {assunto}")

# falar_algo("Livros")

# Inicializador de classe
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def apresentar(self):
        print(f'''
        Nome: {self.nome}
        Idade: {self.idade}
        Altura: {self.altura}
        ''')

pablo = Pessoa("Pablo", 17, 1.68)

pablo.apresentar()
print(f"Só o nome: {pablo.nome}")
print(f"Só a idade: {pablo.idade}")
print(f"Só a altura: {pablo.altura}")
    
