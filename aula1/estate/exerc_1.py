# Crie uma classe de CadastroPessoa
# Crie uma classe de Cliente que herde da Classe CadastroPessoa
# a casse CadastroPessoa deve conter um metodo que informa se 
# a pessoa cadastrada é um cliente Vip ou nao
# Exemplo de saida:

"""
cliente.tipo_de_cliente()
cliente_vip.tipo_de_ciente()

Junior é um cliente Normal
Ana é um cliente Vip
"""
class CadastroPessoa:
    def __init__(self,nome, cliente_vip):
        self.nome = nome
        self.vip = cliente_vip

class Cliente(CadastroPessoa):
    def tipo_de_cliente(self):
        if(self.vip != True):
            print(f"{self.nome} é um cliente Normal")
        else:
            print(f"{self.nome} é um cliente Vip")

Cliente(nome="Junior",cliente_vip= False).tipo_de_cliente()
Cliente(nome="Ana",cliente_vip= True).tipo_de_cliente()