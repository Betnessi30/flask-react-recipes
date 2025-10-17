from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-secret-key'

api = Api(app, doc='/docs')

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}

@api.route('/signup')
class SignUpResource(Resource):
    def post(self):
        return {"message": "Signup works!"}, 201

@api.route('/login')
class LoginResource(Resource):
    def post(self):
        return {"message": "Login works!"}, 200

if __name__ == '__main__':
    app.run(debug=True)