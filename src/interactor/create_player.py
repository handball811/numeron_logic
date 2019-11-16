from src.interface.usecase.create_player import player_create_usecase

from src.entry.player import player_entry

from src.repository.player import player_repository

from logging import getLogger

logger = getLogger(__name__)

class player_create(player_create_usecase):
	def __init__(self, repo :player_repository):
		self.__repo = repo
	def exec(self, name :str) -> player_entry:
		model = player_entry(name=name)
		resp  = self.__repo.create(model)
		if resp:
			return model
		raise RuntimeError("create player rejected")