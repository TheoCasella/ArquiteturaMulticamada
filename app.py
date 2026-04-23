from flask import Flask
from src.Apresentacao.livro_controller import livro_bp

app = Flask(__name__)
app.register_blueprint(livro_bp)

if __name__ == '__main__':
    app.run(debug=True)