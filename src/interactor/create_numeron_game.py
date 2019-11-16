from src.interface.usecase.create_game import game_create_usecase
from typing import List

from src.repository.numeron import numeron_game_repository
from src.entry.game import numeron_game_entry
from src.entry.player import player_entry

from logging import getLogger

logger = getLogger(__name__)

class numeron_game_create(game_create_usecase):
	def __init__(self, repo: numeron_game_repository):
		self.__repo = repo
	def exec(self, players :List[player_entry]) -> numeron_game_entry:
		# 諸々の作成前のチェックを行う
		logger.debug("check if players are 2.")
		if len(players) != 2:
			raise NotImplementedError("players must 2. other not permitted.")
		model = numeron_game_entry(players=players, messages=[])
		if self.__repo.create(model):
			# ゲームが登録完了した段階でprocessに追加する
			# process_manager.append_process(model)
			return model
		raise RuntimeError("creating numeron game permitted")
