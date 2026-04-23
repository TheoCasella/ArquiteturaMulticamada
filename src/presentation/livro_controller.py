'''
Recebe as requisições e chama o respectivo serviço
Onde ficam as rotas
'''

from flask import Blueprint, request, jsonify, render_template
from src.application.livro_service import LivroService

livro_bp = Blueprint('livro', __name__)
service = LivroService()

@livro_bp.route('/')
def index():
    return render_template('index.html')

@livro_bp.route('/api/buscar')
def buscar():
    termo = request.args.get('q', '')
    resultado = service.filtrar_livros(termo)
    return jsonify(resultado)

@livro_bp.route('/api/promocao', methods=['POST'])
def promocao():
    # Feature: Aplica 10% de desconto em todos os livros
    atualizados = service.aplicar_desconto_em_massa(10)
    return jsonify(atualizados)