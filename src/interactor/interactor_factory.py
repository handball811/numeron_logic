from src.interactor import (create_numeron_game, create_player, send_to_player, 
	create_stack_message, get_stack_message)
from src.repository import numeron, player, message

from src.driver.python_message import python_message_storage

# driverはSingletonであることが期待されるので、
message_storage = python_message_storage()

def player_create_factory():
	return create_player.player_create(player.player_repository())

def numeron_game_create_factory():
	return create_numeron_game.numeron_game_create(numeron.numeron_game_repository())

def send_to_player_factory():
	return send_to_player.send_to_player(message.message_repository(message_storage))

def stack_message_create_factory():
	return create_stack_message.stack_message_create()

def stack_message_get_factory():
	return get_stack_message.stack_message_get(message.message_repository(message_storage))