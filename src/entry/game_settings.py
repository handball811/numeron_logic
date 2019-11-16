from dataclasses import dataclass

@dataclass
class numeron_game_setting:
	"""
	ヌメロンをする上でのルールを設定する
	勝負の間変更されないことを想定する。
	"""
	# 勝負における桁数
	digit :int = 3
	# 手数の上限
	turn_limit :int = 10

	# 設定する数値を決定するまでの制限時間
	set_numeber_time_limit :int = 90

	# 聞くまでの制限時間
	ask_time_limit :int = 90
	# 答えるまでの制限時間
	reply_time_limit :int = 30
	# 質問時間の合計
	ask_total_limit :int = 300
	# 質問時間として最低限与えられる時間
	ask_min_limit :int = 20

@dataclass
class numeron_player_setting:
	"""
	ヌメロンをする上で、各個人が設定して行く値
	"""
	number :int = -1