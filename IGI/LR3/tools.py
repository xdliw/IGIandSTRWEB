
#sequence[i] is slow O(n^2), how to do O(n)?
#how yield generator works?
#kak ne kostylno init sequence?
#kak decorator rabotaet? func in func in func??

import random as rnd



def conditional_input(data_type: type = None, condition: callable = None, message: str = "") -> type:
	'''
		conditional input

		Args:
			data_type: type = None, condition: callable = None, message: str = ""
		Returns:
			correct input -> type
	
	'''


	again = True
	while again:
		try:
			var = data_type(input(message)) if data_type else input(message)
			again = not condition(var) if condition else False
		except ValueError:
			pass

	return var



def init_sequence_float_generator(size: int):
	
	for i in range(size):
		yield rnd.random()*100


def input_sequence(size: int, data_type: type = None, condition: callable = None, message: str = ""):

	for i in range(size):
		yield conditional_input(data_type,condition,message)

