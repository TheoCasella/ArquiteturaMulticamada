'''
Onde os dados são armazenados, simulando um Banco de Dados
'''

class LivroRepository:
    def __init__(self):
        # Simula o banco de dados em memória
        self._livros = [
            {"id": 1, "titulo": "Clean Code", "autor": "Robert Martin", "preco": 95.0},
            {"id": 2, "titulo": "Design Patterns", "autor": "GoF", "preco": 120.0},
            {"id": 3, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "preco": 45.90},
            {"id": 4, "titulo": "Memórias Postumas", "autor": "Machado de Assis", "preco": 39.90},
            {"id": 5, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "preco": 35.00},
            {"id": 6, "titulo": "Quincas Borba", "autor": "Machado de Assis", "preco": 42.00}
        ]

    def get_all(self):
        return self._livros

    def save(self, livro_dict):
        self._livros.append(livro_dict)