from abc import ABCMeta, abstractmethod
from typing import List
from src.entry.game import game_entry
from src.entry.player import player_entry

class game_create_usecase(metaclass=ABCMeta):
	# playerをもとにgameのデータを作成する
	@abstractmethod
	def exec(self, players :List[player_entry]) -> game_entry:
		pass