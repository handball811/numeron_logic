"""
基本的な機能は、processを走らせて、対戦のロジックを
進めさせること
"""

from src.service.process.game_process import game_process_manager

from src.interactor.interactor_factory import (player_create_factory, 
	numeron_game_create_factory, send_to_player_factory, 
	stack_message_create_factory, stack_message_get_factory)

import threading

class run:
	def __init__(self):
		self.__manager = game_process_manager()
		self.__run_process = threading.Thread(target=self.__manager.run)

		self.__player_handler = player_create_factory()
		self.__players = []

		self.__game_handler = numeron_game_create_factory()
		self.__games   = []
	def __activate(self):
		# activate process
		self.__run_process.start()
	def __deactivate(self):
		self.__manager.stop()
		self.__run_process.join()
	def exec(self):
		self.__activate()
		while True:
			try:
				process_number = self.__manager.get_process_number()
				print("current process number {}".format(process_number))
				print("current player number  {}".format(len(self.__players)))
				print("current game number    {}".format(len(self.__games)))
				s = input(">>> ")
				if s == "q":
					break
				elif s == "c_p":
					print("What is your name?")
					name = input(">>> ")
					self.__players.append(self.__player_handler.exec(name=name))
				elif s == "s_p":
					print("########   show players   ########")
					for i, p in enumerate(self.__players):
						print("{}: {}".format(i, p))
					print("##################################")
				elif s == "c_g":
					print("Select player1")
					p1 = int(input(">>> "))
					print("Select player2")
					p2 = int(input(">>> "))
					self.__games.append(self.__game_handler.exec(players=[
						self.__players[p1], self.__players[p2]
					]))
				elif s == "s_g":
					print("########   show games   ########")
					for i, g in enumerate(self.__games):
						print("{}: {}".format(i, g))
					print("################################")
				elif s == "up":
					print("Select game")
					g = int(input(">>> "))
					self.__manager.append_process(self.__games[g])
			except:
				break
		self.__deactivate()


if __name__ == "__main__":
	r = run()
	r.exec()


