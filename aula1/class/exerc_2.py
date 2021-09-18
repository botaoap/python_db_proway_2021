# Crie uma classe que representa uma pessoa
# A casse devera receber os valores pelo metodo inicializador
# Devera armazenar os valores efazer a apresentacao dessa pessoa
# Devera conter cabeçalho
# Devera conter Rodapé
# Devera conter um metodo para cada tarefa
# Exemplo de saida
#  """
#     Pessoa("Fulano", 25, 1.70).apresentar()
 
#  ******************************** <--- CAbeçalho

#  Olá, meu nome é Fulano eu tenho 25 anos de idade e tenho 1.70 de altura
 
#  ================================ <--- Rodapé
#  """

class Pessoa:

    def __init__(self):
        self.nome = input("Escolha um nome: ")
        self.idade = input("Escolha uma idade: ")
        self.altura = input("Escolha uma altura: ")
    
    def cabecalho(self):
        return "*"*50
    
    def rodape(self):
        return "="*50
    
    def apresentar(self):
        print(f'''
        {self.cabecalho()}
        
        Olá, meu nome é {self.nome}, eu tenho {self.idade} e tenho {self.altura} de altura

        {self.rodape()}
        ''')
        
Pessoa().apresentar()