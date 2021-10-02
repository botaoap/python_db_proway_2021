class Escritor:

    def __init__(self, nome, livros) -> None:
        self.__nome = nome
        self.__livros = livros
    
    @property
    def nome(self):
        return self.__nome

    @property
    def livros_comprehension(self):
        return [livros for livros in self.__livros]
    
    @property
    def livros_for(self):
        for livros in self.__livros:
            print(livros)

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @livros_for.setter
    def livros_for(self, valor):
        self.__livros = valor

escritor = Escritor(nome="Shakspare", livros=["Livro1","Livro2","Livro3"])

print(escritor.nome)
print(escritor.livros_comprehension)
escritor.livros_for

print()

escritor.nome = "Machado de Assis"
escritor.livros_for = ["A","B","C"]
print(escritor.nome)
print(escritor.livros_comprehension)
escritor.livros_for
