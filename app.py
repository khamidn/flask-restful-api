from flask import Flask, request
from flask_restful import Resource, Api
from resources.messages import messages_api

import models

app = Flask(__name__)
app.register_blueprint(messages_api, url_prefix = '/api/v1')
# api = Api(app)



# api.add_resource(messages.MessageList, '/messages')

if __name__ == '__main__':
	models.initialize()
	app.run(debug=True)