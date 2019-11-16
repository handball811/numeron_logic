from typing import List

from src.interface.repository.game import igame_repository

from src.entry.game import numeron_game_entry
from src.entry.player import player_entry

class numeron_game_repository(igame_repository):
	def create(self, numeron :numeron_game_entry) -> bool:
		# playerが正しいかとかをチェックした方が良さげだけど...
		return True