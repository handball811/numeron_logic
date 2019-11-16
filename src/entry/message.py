from dataclasses import dataclass

@dataclass
class abs_mes:
	pass

@dataclass
class basic_mes(abs_mes):
	message :str


@dataclass
class stack_mes(basic_mes):
	"""
	レポジトリに追加して、ユーザーが確認しにくると
	メッセージを受け取れるようにする
	"""
	create_at :int # UnixTIme
	expire_in :int # 有効期限切れまでの時間