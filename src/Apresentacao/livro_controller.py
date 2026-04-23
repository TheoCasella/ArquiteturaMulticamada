from flask import Blueprint, request, jsonify, render_template
from src.Aplicacao.livro_service import LivroService

livro_bp = Blueprint('livro', __name__)
service = LivroService()

@livro_bp.route('/')
def index(): return render_template('index.html')

@livro_bp.route('/api/buscar')
def buscar():
    return jsonify(service.filtrar_livros(request.args.get('q', '')))

@livro_bp.route('/api/promocao', methods=['POST'])
def promocao():
    res = service.aplicar_desconto(10)
    if res is None:
        return jsonify({"status": "erro"}), 400
    return jsonify(res)