from flask import Flask, request, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def Resp(str):
    response = make_response(str, 200)
    response.mimetype = "text/plain"
    return response

class StartPage(Resource):
    def get(self):
        args = request.args
        if args.__len__() > 0:
            name = args.get("name", default="", type=str)
            message = args.get("message", default="", type=str)
            return Resp("Hello {0}! {1}!".format(name, message))
        else:
            return Resp('Rekruto! Давай дружить!')
        
app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}
api.add_resource(StartPage, '/')

if __name__ == '__main__':
    app.run(debug=True)