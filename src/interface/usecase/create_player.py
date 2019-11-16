from abc import ABCMeta, abstractmethod
from typing import List
from src.entry.player import player_entry

class player_create_usecase(metaclass=ABCMeta):
	# playerをもとにgameのデータを作成する
	@abstractmethod
	def exec(self, name :str) -> player_entry:
		pass