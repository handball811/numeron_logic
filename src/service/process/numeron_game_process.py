from src.service.process.process_def import game_processor
from src.entry.game import game_entry
from src.entry.player import player_message_entry
from src.interactor.interactor_factory import send_to_player_factory

import queue
from logging import getLogger

logger = getLogger(__name__)

class numeron(game_processor):
	def __init__(self, game :game_entry, message_queue :queue.Queue = queue.Queue()):
		self.__game = game
		self.__messages = message_queue
		self.__players = game.players
		self.__mes_sender = send_to_player_factory()
	def process(self) -> bool:
		logger.debug("process came")
		logger.debug("message size {}".format(self.__messages.qsize()))
		# 基本的には入力された値をみて、諸々の操作を行
		# self.__messages.join()
		while not self.__messages.empty():
			message = self.__messages.get()
			logger.debug("new message: {}".format(message))
			_player  = message.player
			_message = message.message
			if _player in self.__players:
				logger.debug("player message got")
				# 同じ内容をこのプレイヤー以外の人に送信する
				for player in self.__players:
					logger.debug("send message to {}".format(player))
					self.__mes_sender.exec(player=player, message=_message)
		# ひとまず、メッセージが自分のユーザーからきたら終了するようにしてみる。
		return True
	def remove(self):
		# 後処理を行う
		return