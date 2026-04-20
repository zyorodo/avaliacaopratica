from flask import Flask, jsonify, abort
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Maria"},
    {"id": 2, "nome": "João"},
    {"id": 3, "nome": "Ana"}
]

@app.route('/')
def home():
    return "API de Usuários ativa! Use a rota /usuarios para listar todos."

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario_por_id(usuario_id):

    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    
    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado"}), 404
        
    return jsonify(usuario), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
