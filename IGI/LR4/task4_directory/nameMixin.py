
class NameMixin:

	def __init__(self, name):
		self.__name = name

	def get_name(self):
		return self.__name
	
	def set_name(self, name : str):
		self.__name = name