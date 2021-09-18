# Cria uma classe que representa uma calculadora
# A classe deve receber os valores a serem calculados pelo metodo inicializador
# DEve conter os 4 calculos basicos
# - Somar
# - Subtrair
# - Dividir
# - Multiplicar


class Calculadora:

    def __init__(self, primeiro_valor, segundo_valor):
        self.primeiro_valor = primeiro_valor
        self.segundo_valor = segundo_valor

    def somar(self):
        return self.primeiro_valor + self.segundo_valor
    

    def subtrair(self):
        return self.primeiro_valor - self.segundo_valor

    
    def multiplicar(self):
        return self.primeiro_valor * self.segundo_valor

    
    def dividir(self):
        if (self.segundo_valor != 0):
            return self.primeiro_valor / self.segundo_valor
        return "Segundo valor n pode ser ZERO"
            

print(Calculadora(1,2).somar())
print(Calculadora(1,2).subtrair())
print(Calculadora(1,2).multiplicar())
print(Calculadora(1,1).dividir())