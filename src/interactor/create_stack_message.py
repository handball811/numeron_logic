from src.interface.usecase.create_stack_message import stack_message_create_usecase
from src.entry.message import stack_mes
from logging import getLogger
import time

logger = getLogger(__name__)


class stack_message_create(stack_message_create_usecase):
	def exec(self, message :str, expire_in :int):
		"""
		これ自体は保存しない
		"""
		if expire_in < 0:
			expire_in = 0
			logger.warning("expire_in must set 0 or positive number")
		model = stack_mes(message=message, create_at=time.time(), expire_in=expire_in)
		print(model)
		return model
