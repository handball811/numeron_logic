
from abc import ABCMeta, abstractmethod
from src.entry.game import game_entry
import queue
class game_processor(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, game :game_entry, message_queue :queue.Queue = queue.Queue()):
		pass
	@abstractmethod
	def process(self) -> bool:
		"""
		もし返却値がFalseならこのプロセスを終了する
		"""
		pass
	@abstractmethod
	def remove(self):
		pass