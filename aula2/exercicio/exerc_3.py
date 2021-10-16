# Crie uma classe de cadastro de Pessoa usando o classmethod
# essa classe devera ter um atributo chamando banco_de_dados que sera um dicionario vazio
# a classe deve Cria o cadastro de clientes com `nome idade id`
# o id devera ser auto gerado se tiver um cliente com id 1 o prox devera conter o id 2
#
# Exemplo
#
# CadastroCLiente.criar_cadastro(nome, idade)
# Cadastro.listar_clientes()

"""
>>> {
        clientes: {
            id:1, nome:"Fulano", idade:25,
            id:2, nome:"FulanoDeTal", idade:55,
            id:3, nome:"FooBar", idade:65
        }
    }
"""

class Pessoa:

    # dictionary = {
    #     id:"",
    #     nome:"",
    #     idade:""
    # }
    def __init__(self, pessoa) -> None:
        # self.id = 0
        # self.nome = nome_pessoa
        # self.idade = idade_pessoa
        # self.pessoa = pessoa 
        # clientes = {
        #     "id": 0,
        #     "nome": nome_pessoa,
        #     "idade": idade_pessoa
        # }
        self.pessoa = pessoa
    cliente = {
            'cliente': {}
        }
    @classmethod
    def banco_de_dados(cls,id, nome_pessoa, idade_pessoa):
        db_pessoa = {id: {
                'nome': nome_pessoa,
                'idade': idade_pessoa
            }   
        }
        
        cls.cliente['cliente'].update(db_pessoa)

        # db_pessoa['id'] = id
        # db_pessoa['nome'] = nome_pessoa
        # db_pessoa['idade'] = idade_pessoa

        return cls(cls.cliente)
    
    def ler_pessoa(self):
        return self.pessoa
    

# pessoa = Pessoa.banco_de_dados(0,nome_pessoa="jorge",idade_pessoa= 11)
# pessoa1 = Pessoa.banco_de_dados(1,nome_pessoa="jorge2",idade_pessoa= 12)

cont = 0
while (True):
    nome = input("Cadastre um nome: ")
    idade = int(input("Cadastre uma idade: "))
    
    cont = cont + 1

    total_pessoas = Pessoa.banco_de_dados(cont, nome, idade)
    sair = input('Pressione "S" para sair: ' )
    if (sair == "S" or sair == "s"):
        try:
            break
        except:
            continue 

print(total_pessoas.ler_pessoa())