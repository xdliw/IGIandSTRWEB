import math
import tools
import my_decorator as md

def calculate_taylor(x, eps):
	"""
			A function that finds ln using a power series expansion.

			Args:
					x (float): The value of x for which the sum of the series is calculated.
					eps (float): The accuracy with which the value of ln((x + 1)/(x - 1)) is to be obtained.
			
			Returns:
					float: res
					int: The number of iterations.
	"""


	i = 0
	res = 0
	prec = math.inf
	prev = math.inf
	while i < 500 and prec > eps:
		cur = 2/((2*i + 1) * x ** (2*i + 1))
		res += cur
		prec = abs(cur - prev)
		prev = cur
		i += 1

	return res, i


@md.my_decorator("task1")
def task1():
	"""
			task1 

			Calculates taylor_series logarithm, outputs it and some tech info.
	"""

	eps = tools.conditional_input(float,None,"input eps = float ")
	x = tools.conditional_input(float, lambda x:abs(x) > 1,"input |x| > 1 = float ")

	res, i = calculate_taylor(x, eps)

	print(f"x = {x} n = {i} F(x) = {res} Math F(x) = {math.log((x + 1)/(x - 1), math.e)} eps = {eps}")

