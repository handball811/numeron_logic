from src.interface.usecase.get_stack_message import stack_message_get_usecase
from src.entry.player import player_entry
from src.repository.message import message_repository

from src.entry.message import stack_mes
from typing import List

class stack_message_get(stack_message_get_usecase):
	def __init__(self, repo: message_repository):
		self.__repo = repo
	def exec(self, player :player_entry) -> List[stack_mes]:
		ret = self.__repo.get(player=player)
		return ret