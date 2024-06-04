
class Figure_color:

	def __init__(self, value : str):
		self.__value = value

	@property
	def value(self):
		return self.__value
	
	@value.setter
	def value(self, value):
		self.__value = value