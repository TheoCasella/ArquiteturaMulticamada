'''
Onde a lógica do código acontece, como por exemplo filtrar livros, aplicar desconte
'''

from src.infrastructure.livro_repository import LivroRepository

class LivroService:
    def __init__(self):
        self.repo = LivroRepository()
        self.desconto_aplicado = False

    def filtrar_livros(self, termo):
        todos = self.repo.get_all()
        if not termo:
            return todos
        return [l for l in todos if termo.lower() in l['titulo'].lower()]

    def aplicar_desconto_em_massa(self, percentual):
        if self.desconto_aplicado:
            return self.repo.get_all()

        livros = self.repo.get_all()
        for l in livros:
            l['preco'] -= (l['preco'] * (percentual / 100))

        self.desconto_aplicado = True
        return livros