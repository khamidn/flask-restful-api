from flask import jsonify
from flask_restful import Resource

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