

def conditional_input(data_type: type = None, condition: callable = None, message: str = "") -> type:
	'''\
Input with requirements.

data_type:\t what type is allowed as input
condition:\t additional requirements for input
message:\t prints every time input is asked (first time or in case if incorrect)
	'''

	again = True
	while again:
		try:
			var = data_type(input(message)) if data_type else input(message)
			again = not condition(var) if condition else False
		except ValueError:
			pass

	return var



def input_sequence(size: int, data_type: type = None, condition: callable = None, message: str = ""):

	for i in range(size):
		yield conditional_input(data_type,condition,message)
