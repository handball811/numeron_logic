import pytest

from src.interactor.interactor_factory import (player_create_factory, 
	numeron_game_create_factory, send_to_player_factory, 
	stack_message_create_factory, stack_message_get_factory)

from src.entry.player import player_message_entry
from src.entry.message import stack_mes

from src.service.process.game_process import game_process_manager
from src.driver.python_message import python_message_storage

import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG)

@pytest.mark.player
def test_create_player():
	# playerを生成する
	inter = player_create_factory()
	user  = inter.exec(name="sasakuna")
	assert user.name == "sasakuna"

@pytest.mark.numeron
def test_create_numeron():
	# Numeron make game
	# First create player
	p_in    = player_create_factory()
	user1   = p_in.exec(name="sasakuna")
	user2   = p_in.exec(name="nobura")
	user3   = p_in.exec(name="kobura")
	# make game instance
	inter   = numeron_game_create_factory()
	with pytest.raises(NotImplementedError) as e_info:
		numeron = inter.exec(players=[user1, user2, user3])
	numeron = inter.exec(players=[user1, user2])
	print(numeron)
	print(numeron.process_state)
	assert len(numeron.players) == 2
	# 勝負における設定桁数
	assert numeron.settings.digit == 3
@pytest.mark.message
def test_message():
	# Message make
	message = "hi sasakuna!"
	expire_time = 3600
	#
	p_in  = player_create_factory()
	user  = p_in.exec(name="sasakuna")
	m_in  = stack_message_create_factory()
	mes   = m_in.exec(message=message, expire_in=expire_time)
	assert mes.__class__ == stack_mes
	assert mes.message == message
	assert mes.expire_in == expire_time
	assert time.time() - mes.create_at < 5
	inter = send_to_player_factory()
	send  = inter.exec(user, mes)
	print(send)
	print(send.player)
	print(send.message)
	assert send.message.message == message
	assert send.player.name == "sasakuna"

@pytest.mark.process
def test_process():
	message = "message"
	expire_time = -100
	pmes_storage = python_message_storage()
	p_in    = player_create_factory()
	user1   = p_in.exec(name="sasakuna")
	user2   = p_in.exec(name="nobura")
	user3   = p_in.exec(name="kobura")
	# make game instance
	inter   = numeron_game_create_factory()
	with pytest.raises(NotImplementedError) as e_info:
		numeron = inter.exec(players=[user1, user2, user3])
	numeron = inter.exec(players=[user1, user2])

	process_manager = game_process_manager()

	# プロセスの起動
	p_run = threading.Thread(target=process_manager.run)
	p_run.start()
	assert process_manager.get_process_number() == 0
	process_manager.append_process(numeron)
	# プロセスの追加が2回目なのでアラートが出るはず
	with pytest.raises(RuntimeError) as e_info:
		process_manager.append_process(numeron)
	assert process_manager.get_process_number() == 1
	time.sleep(2)

	m_in  = stack_message_create_factory()
	mes   = m_in.exec(message=message, expire_in=expire_time)
	process_manager.set_message(numeron, user3, mes)
	time.sleep(2)

	mes   = m_in.exec(message=message, expire_in=expire_time)
	process_manager.set_message(numeron, user1, mes)
	time.sleep(3)
	assert process_manager.get_process_number() == 1

	# 一時的な機能
	assert pmes_storage.exists(user2)
	assert pmes_storage.exists(user1)

	smes_get = stack_message_get_factory()
	mes = smes_get.exec(user1)

	assert len(mes) == 1
	assert not pmes_storage.exists(user1)





	process_manager.stop()
	p_run.join()









