"""

このプロセスを回すことで複数の登録されたゲームを進行させる。

"""
from src.entry.game import game_entry
from src.entry.message import basic_mes
from src.entry.player import player_entry, player_message_entry
from src.service.process.game_process_factory import game_factory
from src.module.singleton import Singleton
import queue
import time

from logging import getLogger

logger = getLogger(__name__)


class game_process_manager(Singleton):
	MAX_PROCESS_LEN = 16
	PROCESS_INTERVAL = 1.0
	def __init__(self):
		"""
		ゲームプロセスを追加したり、動かしたりしている
		"""
		self.__cancellation_flag = False
		self.__process = {} # game_processor
		self.__message_queues = {}
	def stop(self):
		self.__cancellation_flag = True

	def run(self):
		"""
		ここが定常プロセスになる
		stop関数を起動すると、停止するようにする
		"""
		self.__cancellation_flag = False
		try:
			while not self.__cancellation_flag:
				_start_time = time.time()
				_removeing = []
				###########   INTERVAL ADJUSTING       ##########
				# プロセスを動かすパート
				for _uuid, _process in self.__process.items():
					ret = _process.process()
					if not ret:
						_removeing.append(_uuid)
				# 削除を依頼されたプロセスを削除する
				for _uuid in _removeing:
					self.__remove_process(_uuid)
				###########   INTERVAL ADJUSTING END   ##########
				_req_interval = self.PROCESS_INTERVAL - time.time() + _start_time
				if _req_interval > 0.1:
					time.sleep(_req_interval)
		except:
			# プロセスの突然お終了で、正規の処理ができなくなることを避けるために
			# 簡易的な例外処理を行う
			import traceback
			traceback.print_exc()

		# 終了とともに全てのプロセスを終了する
		_removeing = [_uuid for _uuid in self.__process.keys()]
		for _uuid in _removeing:
			self.__remove_process(_uuid)

	def __remove_process(self, _uuid :str) -> bool:
		if not _uuid in self.__process:
			return False
		try:
			self.__process[_uuid].remove()
		except:
			import traceback
			traceback.print_exc()
		del(self.__message_queues[_uuid])
		del(self.__process[_uuid])
		return True

	def get_process_number(self):
		return len(self.__process)

	def append_process(self, game :game_entry):
		"""
		プロセスの追加処理を行う
		"""
		logger.debug("check if process can be added, with the dimention of process number that is currently working.")
		if self.get_process_number() > self.MAX_PROCESS_LEN:
			raise RuntimeError("sorry, process reached maximum number")

		logger.debug("check if input game has already worked")
		logger.debug("input game uuid is {}".format(game.uuid))
		logger.debug("currently working processes are {}".format(
			", ".join([p for p in self.__process.keys()])))
		if game.uuid in self.__process.keys():
			raise RuntimeError("the process is already activated")

		logger.debug("make new process")
		_queue   = queue.Queue()
		_process = game_factory(game=game, message_queue=_queue)

		self.__message_queues[game.uuid] = _queue
		self.__process[game.uuid] = _process

	def set_message(self, game :game_entry, player :player_entry, message :basic_mes):
		"""
		ゲームプロセスが存在するなら、メッセージを所定のところに追加する。
		"""
		logger.debug("setting new message")
		_uuid = game.uuid
		if _uuid in self.__message_queues.keys():
			logger.debug("set message accepted")
			self.__message_queues[_uuid].put(player_message_entry(player=player,message=message))
		else:
			raise NotImplementedError("your game entry does not set yet")



