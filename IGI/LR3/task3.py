from tools import conditional_input as ci

def task3():
	"""
		Function to perform task 3.
		
		Task 3: In the string entered from the keyboard, count capital vowels
	"""	 
	

	capital_vowels = set(['E','U','I','O','A','Y'])
	input = ci(str,None,"input string\n")
	res = 0
	for c in input:
		res += c in capital_vowels

	print(res)