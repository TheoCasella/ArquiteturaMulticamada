'''
Define o que é um "Livro"
'''

class Livro:
    def __init__(self, id, titulo, autor, preco):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def to_dict(self):
        return self.__dict__