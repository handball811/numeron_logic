from threading import Lock
from abc import ABC
from logging import getLogger

logger = getLogger(__name__)

class Singleton(object):
	_unique_instance = None
	_lock = Lock()
	def __new__(cls):
		logger.debug("creating")
		if not cls._unique_instance:
			with cls._lock:
				if not cls._unique_instance:
					cls._unique_instance = super().__new__(cls)
		return cls._unique_instance
