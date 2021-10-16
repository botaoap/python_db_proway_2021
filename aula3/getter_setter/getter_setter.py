class Escritor:

    def __init__(self, nome, livros ) -> None:
        self.__nome = nome
        self.__livros = livros
    
    def get_nome(self):
        return self.__nome
    
    def get_livros(self):
        # for list comprehension
        return [livro for livro in self.__livros]

    def set_nome(self, valor):
        self.__nome = valor

escritor = Escritor(nome="Alabama",livros=["Livro1", "Livro2","Livro3"])
print(escritor.get_nome())
escritor.set_nome("Machado de Assis")
print(escritor.get_nome())
print(escritor.get_livros())