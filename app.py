from flask import Flask, request
from flask_restful import Resource, Api

from resources.messages import messages_api
from resources.users import users_api


from flask_jwt_extended import (JWTManager, jwt_required, 
								create_access_token, get_jwt_identity)


import models

app = Flask(__name__)
app.register_blueprint(messages_api, url_prefix = '/api/v1')
app.register_blueprint(users_api, url_prefix = '/api/v1')

# ACCESS_TOKEN_JWT
app.config['SECRET_KEY'] = 'randomString_superSecret1928390123'
jwt = JWTManager(app)

if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)