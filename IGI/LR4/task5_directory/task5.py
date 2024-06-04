import numpy as np

def task5():
	#init
	n = 5
	m = 8
	a = 1
	b = 100
	matrix = np.random.randint(a,b,(n,m))
	print("matrix:\n", matrix)

	#fill list C
	B = 50
	C = []
	for row in matrix:
		for el in row:
			if abs(el) > B:
				C.append(el)
	
	#make C into numpy array
	C = np.array(C)

	print("array C:")
	for el in C:
		print(el, end=' ')
	print()

	print("NumPy median:", np.median(C))

	#count median
	C = np.sort(C)
	mid = len(C) // 2

	if len(C) & 1:
		median = C[mid] / 1
	else:
		median = (C[mid - 1] + C[mid]) / 2

	print("My median: ", median)


if __name__ == "__main__":
	task5()