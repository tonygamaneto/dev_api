from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import habilidades

app= Flask(__name__)
api = Api(app)

desenvolvedores =  [
    {'id':0, 'nome': 'Rafael','habilidades':['python', 'flask']},
    {'id':1, 'nome': 'Galeani','habilidades':['Python', 'Django']}
]
#devolve um desenvolvedor pelo ID, tambem altera e deleta registro

class Desenvolvedor(Resource):
    def get(self,id):
        try :
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id : {} nao existe'.format(id)

            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return response


    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso', 'Mensagem': 'Registro Excluido'}


# Lista de todos desenvolvedores e inclui um novo desenvolvedor
class lista_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):

        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(lista_desenvolvedores, '/dev/')
api.add_resource(habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)
