from flask import Flask, jsonify, request
import os

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Joao"},
    {"id": 3, "nome": "Carlos"}
]

@app.route("/alunos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Alunos - Acesse/Alunos"})

@app.route("/alunos", methods=["GET"])
def listar_alunos(): 
    return jsonify (alunos)

@app.route("/alunos", methods=["POST"])
def criar_aluno():
    novo = request.json
    novo['id'] = len(alunos) + 1
    alunos.append(novo)
    return jsonify(novo), 201

@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    dados_atualizados = request.json
    for aluno in alunos:
        if aluno["id"] == id:
            aluno["nome"] = dados_atualizados.get("nome", aluno["nome"])
            return jsonify(aluno), 200
    return jsonify({"erro": "Aluno não existe"}), 404

@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify({"mensagem": "Aluno removido"}), 200
    return jsonify({"erro": "Aluno nao existe"}), 404


if __name__ == '__main__':
 app.run(debug=True)
 