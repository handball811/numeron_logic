from dataclasses import dataclass, field
from typing  import List, Dict

from src.entry.player import player_entry, player_message_entry
from src.entry.game_settings import numeron_game_setting, numeron_player_setting

from uuid import uuid4

@dataclass(frozen=True, eq=True)
class game_entry:
	# game_id
	uuid     :str = field(init=False)
	# player
	players  :List[player_entry]
	# messages
	messages :List[player_message_entry]
	def __post_init__(self):
		object.__setattr__(
			self,
			"uuid",
			str(uuid4()))

@dataclass(frozen=True, eq=True)
class numeron_game_entry(game_entry):
	# 設定ファイル
	settings :numeron_game_setting = numeron_game_setting()
	# 現在の状態をわかりやすく管理するための方法
	process_state :str = field(init=False)
	# ゲームで設定した番号が何であるかを保存する
	player_settings :Dict[player_entry, numeron_player_setting] = field(default_factory=dict,init=False)

	def __post_init__(self):
		super().__post_init__()
		if len(self.players) != 2:
			raise NotImplementedError("player number must be 2.")
		object.__setattr__(
			self,
			"player_settings",
			{player:numeron_player_setting() for player in self.players})
		object.__setattr__(
			self,
			"process_state",
			"init:num:"+":".join(["p"+str(i) for i in range(len(self.players))]))


