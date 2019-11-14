from flask import Flask
from flask_restful import Resource, Api
from events import alt_tab

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Alert(Resource):
    def get(self):
        alt_tab()
        return {'info': 'alert received!'}

api.add_resource(HelloWorld, '/')
api.add_resource(Alert, '/alert')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
