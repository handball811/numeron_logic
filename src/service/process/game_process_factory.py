from src.service.process import numeron_game_process
from src.entry.game import game_entry, numeron_game_entry

import queue

def game_factory(game :game_entry, message_queue :queue.Queue = queue.Queue()):
	"""
	game entry のクラスで分類する
	"""
	game_type = game.__class__
	if game_type == numeron_game_entry:
		_process = numeron_game_process.numeron(game, message_queue)
	else:
		raise NotImplementedError("your requested process not known.")
	return _process
