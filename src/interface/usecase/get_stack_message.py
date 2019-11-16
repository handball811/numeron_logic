from abc import ABCMeta, abstractmethod
from src.entry.player import player_entry
from src.repository.message import message_repository
from src.entry.message import stack_mes
from typing import List


class stack_message_get_usecase(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, repo :message_repository):
		pass
	@abstractmethod
	def exec(self, player :player_entry) -> List[stack_mes]:
		pass