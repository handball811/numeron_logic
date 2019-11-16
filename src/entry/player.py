from dataclasses import dataclass
from src.entry.message import abs_mes

@dataclass(frozen=True, eq=True)
class player_entry: 
	name :str

@dataclass
class player_message_entry:
	# 入力してきたプレイヤー情報
	player  : player_entry
	# メッセージの内容
	message : abs_mes

@dataclass
class player_input_entry(player_message_entry):
	pass

@dataclass
class player_output_entry(player_message_entry):
	pass
