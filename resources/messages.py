from flask import jsonify, Blueprint
from flask_restful import Resource, Api

import models

class MessageList(Resource):
	def get(self):
		#ambil data dari db
		messages = {}
		query = models.Message.select()

		for row in query:
			messages[row.id] = {'content': row.content,
								'published_at': row.published_at
								}
		return jsonify({'messages' : messages})



messages_api = Blueprint('resources.messages', __name__)
api = Api(messages_api)

api.add_resource(MessageList, '/messages', endpoint='messages')