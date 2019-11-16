from abc import ABCMeta, abstractmethod
from typing import List

from src.entry.player import player_entry
from src.entry.message import basic_mes

class send_to_player_usecase(metaclass=ABCMeta):
	# playerのもとにメッセージを送る
	# 設定されているメッセージの種類によって挙動をかえる
	@abstractmethod
	def exec(self, player :player_entry, message :basic_mes):
		pass
