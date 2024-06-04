from abc import ABC, abstractmethod

class Serializer(ABC):
	@classmethod 
	@abstractmethod
	def serialize(cls, synonyms: dict[str,str], path: str):
		pass

	@classmethod 
	@abstractmethod
	def deserialize(cls, path: str):
		pass

