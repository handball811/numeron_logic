from abc import ABCMeta, abstractmethod
from src.entry.player import player_message_entry
from src.interface.driver.message import message_storage

class imessage_repository(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, driver :message_storage):
		pass
	@abstractmethod
	def create(self, player_message :player_message_entry) -> bool:
		# メッセージを保管する
		# 実際には、データベースに保管するのだが、いまはできない...
		# 成功失敗を表す値を返答する
		pass
	@abstractmethod
	def get(self, *args, **kwargs):
		"""
		条件は色々...
		"""
		pass

