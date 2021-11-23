from flask import Flask, jsonify, request
import  json
app = Flask(__name__)

desenvolvedores =  [
    {'id':0, 'nome': 'Rafael','habilidades':['python', 'flask']},
    {'id':1, 'nome': 'Galeani','habilidades':['Python', 'Django']}
]

@app.route ('/dev/<int:id>/', methods =['GET', 'PUT', 'DELETE'])

#devolve um desenvolvedor pelo ID, tambem altera e deleta registro

def desenvolvedor (id):
    if request.method =='GET':
        try :
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id : {} nao existe'.format(id)

            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return jsonify (response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method =='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso', 'Mensagem':'Registro Excluido'})

# Lista de todos desenvolvedores e inclui um novo desenvolvedor
@app.route ('/dev/', methods =['POST', 'GET'])

def lista_desenvolvedores():
    if request.method=='POST':
        dados =  json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
    elif request.method == 'GET':
        return jsonify (desenvolvedores)


    return  jsonify(desenvolvedores[posicao])



if __name__ == '__main__':
    app.run(debug=True)
