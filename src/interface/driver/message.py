from abc import ABC, ABCMeta, abstractmethod
from src.module.singleton import Singleton
from src.entry.player import player_entry, player_message_entry
from typing import List

class message_storage(ABC, Singleton):
	@abstractmethod
	def set_message(self, player_message :player_message_entry):
		pass
	@abstractmethod
	def get_all_message(self, player :player_entry) -> List[player_message_entry]:
		pass
	@abstractmethod
	def exists(self, player :player_entry) -> bool:
		pass