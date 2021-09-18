# Crie uma classe de cadastro de Produtos
# Essa classe devera herdar da CLasse Categoria

# Devera imprimir na tela para cada Produto com a classe Categoria

# class Categoria:
#     def __init__(self, category_name):
#         self.category_name = category_name

# class Produto(Categoria):
    
#     def __init__(self, category_name, procuct_name, price):
#         super().__init__(category_name)
#         self.product_name = procuct_name
#         self.price = price
    
#     def result_produto(self):
#         dict_product = {
#             'product': self.product_name,
#             'price': self.price,
#             'category': self.category_name
#         }
#         print(dict_product)

# Produto(procuct_name="Sabao em po", price=19.90, category_name="Limpeza").result_produto()

class Categoria:
    def __init__(self, category_name):
        self.category_name = category_name

class Produto:
    
    def __init__(self, procuct_name, price):
        self.product_name = procuct_name
        self.price = price
    
    def result_produto(self, category):
        dict_product = {
            'product': self.product_name,
            'price': self.price,
            'category': category
        }
        print(dict_product)

categoria = Categoria("Limpeza").category_name

Produto(procuct_name="Sabao em po", price=10.90).result_produto(category=categoria)