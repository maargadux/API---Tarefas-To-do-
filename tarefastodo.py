#tarefas to-do
from flask import Flask, jsonify, request
app = Flask(__name__)

tarefas = [
    {
        'id': 1,
        'tarefa': 'Tomar café',
        'concluido': False
    },
    {
        'id': 2,
        'tarefa': 'Estudar Python',
        'concluido': False
    },
    {
        'id': 3,
        'tarefa': 'Fazer exercícios',
        'concluido': False
    },
    {
        'id': 4,
        'tarefa': 'Ler um livro',
        'concluido': False
    }
]

#consultar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify({'tarefas': tarefas})
#consulta uma tarefa
@app.route('/tarefas/<int:id>', methods=['GET'])
def get_tarefa(id):
    tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == id), None)
    if tarefa:
        return jsonify({'tarefa': tarefa})
    return jsonify({'message': 'Tarefa não encontrada'}), 404
#adicionar uma tarefa
@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify({'message': 'Tarefa adicionada com sucesso'}), 201
#editar uma tarefa
@app.route('/tarefas/<int:id>', methods=['PUT'])
def update_tarefa(id):
    tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == id), None)
    if tarefa:
        dados = request.get_json()
        tarefa.update(dados)
        return jsonify({'message': 'Tarefa atualizada com sucesso'})
    return jsonify({'message': 'Tarefa não encontrada'}), 404
#excluir uma tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def delete_tarefa(id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != id]
    return jsonify({'message': 'Tarefa excluída com sucesso'})
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)