from src.interface.repository.message import imessage_repository
from src.entry.player import player_message_entry
from src.entry.message import basic_mes
from src.interface.driver.message import message_storage

class message_repository(imessage_repository):
	def __init__(self, driver :message_storage):
		self.__driver = driver
	def create(self, player_message :player_message_entry) -> bool:
		self.__driver.set_message(player_message)
		return True
	def get(self, *args, **kwargs) -> [basic_mes]:
		resp = []
		if self.__driver.exists(player=kwargs["player"]):
			resp = self.__driver.get_all_message(player=kwargs["player"])
		return resp
