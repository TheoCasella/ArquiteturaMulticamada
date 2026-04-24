from abc import ABC, abstractmethod

# Define O QUE deve ser feito, mas não COMO.
class IRepositorioLivro(ABC):

    @abstractmethod
    def get_all(self):
        """Retorna todos os livros do banco de dados real"""
        pass

    @abstractmethod
    def save(self, livro):
        """Salva um novo livro no banco de dados real"""
        pass


class LivroRepository(IRepositorioLivro):
    def __init__(self, conexao_banco=None):
        self.db = conexao_banco

    def get_all(self):
        # Simulando onde entraria a lógica de banco real
        # Exemplo: return self.db.execute("SELECT * FROM livros")
        print("Buscando dados no Banco de Dados Real...")
        return []  # Retorna vazio por enquanto já que não há banco real

    def save(self, livro):
        # Exemplo: self.db.execute("INSERT INTO...", livro)
        print(f"Salvando o livro '{livro['titulo']}' no Banco de Dados Real...")