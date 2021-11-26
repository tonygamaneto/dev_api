from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth
import json

auth= HTTPBasicAuth()
app = Flask(__name__)
api =  Api(app)

'''USUARIOS = {
    'Rafael':'123',
    'Galeani': '321'
}'''

@auth.verify_password
def verificacao(login, senha):
    print('Validando usuario ')
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa (Resource):
    @auth.login_required()

    def get(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try :
            response = {
                'nome':pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'Status':'erro',
                'mensagem': 'pessoa nao encontrada'}
        return response


    def put(self,id):
        dados = json.loads(request.data)
        Pessoas[id] = dados
        return dados

    def delete(self,id):
        Pessoas.pop(id)
        return {'status': 'Sucesso', 'Mensagem': 'Registro Excluido'}


# Lista de todos desenvolvedores e inclui um novo desenvolvedor
class lista_Pessoas(Resource):
    def get(self):
        return Pessoas

    def post(self):
        dados = request.json
        pessoa=Pessoas.query.filter_by(nome=dados['pessoa']).first
        atividade= Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response= [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

        dados = json.loads(request.data)
        posicao = len(Pessoas)
        dados['id'] = posicao
        Pessoas.append(dados)
        return Pessoas[posicao]


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(lista_Pessoas,'/pessoa/')
api.add_resource(ListaAtividades, '/atividaes/')

#api.add_resource(Pessoa,'/pessoa/<int:id>/')
#api.add_resource(lista_desenvolvedores, '/dev/')



if __name__ == '__main__':
    app.run(debug=True)
