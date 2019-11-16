from abc import ABCMeta, abstractmethod
from src.entry.player import player_entry

class iplayer_repository(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self):
		pass
	@abstractmethod
	def create(self, player :player_entry) -> bool:
		pass