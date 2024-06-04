def calculate_taylor(x : float, n : int, create_list : bool = False):
	"""
			A function that finds ln using a power series expansion.

			Args:
					x (float): The value of x for which the sum of the series is calculated.
			
			Returns:
					float: res
	"""

	i = 0
	res = 0
	li = []
	while i <= n:
		term = 2/((2*i + 1) * x ** (2*i + 1))
		res += term
		i += 1
		if create_list:
			li.append(term)
		
	if create_list:
		return res,li
	return res
