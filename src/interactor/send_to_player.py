from src.interface.usecase.send_to_player import send_to_player_usecase
from src.repository.message import message_repository

from src.entry.message import basic_mes, stack_mes
from src.entry.player import player_entry, player_message_entry

class send_to_player(send_to_player_usecase):
	def __init__(self, repo: message_repository):
		self.__repo = repo
	def exec(self, player :player_entry, message :basic_mes):
		mes_type = message.__class__
		if mes_type == stack_mes:
			model = player_message_entry(player=player, message=message)
			resp  = self.__repo.create(model)
		else:
			raise ValueError("message type not expected")
		if resp:
			return model
		raise RuntimeError("create message rejected")
