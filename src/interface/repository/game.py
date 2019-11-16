from abc import ABCMeta, abstractmethod
from typing import List
from src.entry.game import game_entry
from src.entry.player import player_entry

class igame_repository(metaclass=ABCMeta):
	# ゲームのインスタンスを管理する部分
	@abstractmethod
	def create(self, players :game_entry) -> bool:
		# インスタンスの生成を行なってください
		pass