
from tools import conditional_input as ci

def task2():
	"""
		task 2

		Calculates minimum number
	"""

	input = ci(int,None,"input integer or 0 to exit")
	minimum = input
	while input:
		minimum = min(minimum,input)
		input = ci(int,None,"input integer or 0 to exit")
	
	print(minimum)