from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0', 'nome': 'Micael', 'habilidades': ['Pythom', 'Pandas']},
    {'id': '1', 'nome': 'Ze', 'habilidades': ['Python', 'Flask']}
]

# devolve, altera e delete um desenvolvedor conforme ID enviado


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {
                'status': 'Erro', 'mensagem': 'Desenvolvedor de ID {} não existe' .format(id)}
        except Exception:
            response = {'status': 'Erro', 'mensagem': 'Parabens quebrou tudo'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro eliminado'})

# lista e cria todos os desenvolvedores


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
