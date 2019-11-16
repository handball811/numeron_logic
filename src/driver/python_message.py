from src.interface.driver.message import message_storage
from src.entry.player import player_entry, player_message_entry
from src.entry.message import basic_mes
from typing import List

from logging import getLogger

logger = getLogger(__name__)

class python_message_storage(message_storage):
	def __init__(self):
		self.__messages = {}

	def set_message(self, player_message :player_message_entry):
		logger.debug("message try to set")
		_player  = player_message.player
		_message = player_message.message
		logger.debug("player:{} message:{}".format(_player, _message))
		if _player in self.__messages.keys():
			self.__messages[_player].append(_message)
		else:
			self.__messages[_player] = [_message]
		logger.debug("current messages in set_message is {} ({})".format(self.__messages, self))
	def get_all_message(self, player :player_entry) -> List[basic_mes]:
		# 今の所、expireのタイミングは見ていない
		ret = self.__messages[player]
		del(self.__messages[player])
		return ret
	def exists(self, player :player_entry) -> bool:
		logger.debug("current messages in exists is {} ({})".format(self.__messages, self))
		return player in self.__messages.keys() and len(self.__messages[player])>0