import tools


def task5():
	"""
		Function to perform task 5.

		Task 5:
		Найти количество элементов списка, лежащих в диапазоне от А до В 
		(параметры A и B вводятся с клавиатуры пользователем) 
		и сумму элементов списка, расположенных после максимального элемента.

	"""


	use_generator = tools.conditional_input(int, lambda x: 0 <= x <= 1, "0 to input from keyboard,\n1 to use random generator\n")
	
	size = tools.conditional_input(int, lambda x: x >= 0, "input size for a sequence\n")
	

	if use_generator:
		seq = list(tools.init_sequence_float_generator(size))
	else:
		seq = list(tools.input_sequence(size,float,None,"input remaining numbers\n"))

	print(f"your sequence: {seq}")

	A = tools.conditional_input(int,None,"input A\n")
	B = tools.conditional_input(int,None,"input B\n")

	max_element_pos = 0
	max_element = seq[0]
	count = 0
	
	for i, num in enumerate(seq):
		if A <= num <= B:
			count += 1
		if num > max_element:
			max_element = num
			max_element_pos = i

	
	sum = 0
	for i in range(max_element_pos + 1,len(seq)):
		sum += seq[i]

	print(f"amount of elements in range [{A},{B}] = {count}")
	print(f"sum of elements after maximal element = {sum}")

	
