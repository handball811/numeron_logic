from abc import ABCMeta, abstractmethod

class stack_message_create_usecase(metaclass=ABCMeta):
	@abstractmethod
	def exec(self, message :str, expire_in :int):
		pass