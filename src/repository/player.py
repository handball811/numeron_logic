from src.interface.repository.player import iplayer_repository
from src.entry.player import player_entry

class player_repository(iplayer_repository):
	def __init__(self):
		pass
	def create(self, player :player_entry) -> bool:
		return True