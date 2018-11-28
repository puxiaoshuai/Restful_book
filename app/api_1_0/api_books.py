from flask import Blueprint

from flask_restful import Resource, Api, reqparse, marshal_with, fields

bp_book = Blueprint('book', __name__, url_prefix='/book/api')
from app_book import create_app

app = create_app()
api = Api(app=app)


class HelloWorld(Resource):
    def get(self):
        return {"username": '蒲小帅'}


api.add_resource(HelloWorld, '/hello/', endpoint='login')


class SayHello(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("name", trim=True, required=True, type=str, default="王麻子", help="参数错误")
        # 获取传过来的参数值
        args = parse.parse_args()
        content = {
            'username': args.get('name')
        }
        return content


api.add_resource(SayHello, '/sayhello/', endpoint='sayhello')


class ArticleView(Resource):
    res_fields = {
        'name': fields.String(default="姓名", attribute='username')
        , 'content': fields.String(default="11")
    }

    @marshal_with(res_fields)
    def get(self):
        pass
