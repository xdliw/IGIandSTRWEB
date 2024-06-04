if __name__ == "__main__":
	import os
	import sys

	sys.path.append(os.path.dirname(__file__) + "/..")

from task3_directory.calculate_taylor import calculate_taylor
from tools.tools import conditional_input
from task3_directory.save_graph import save_graph
import math
import numpy
import statistics


def task3():
	x = conditional_input(float, lambda x: abs(x) > 1, "Enter |x| > 1: ")
	n = conditional_input(int, lambda x: x > 1,"Enter n > 1: ")
	f, arr = calculate_taylor(x, n, True)
	math_f = math.log((x + 1)/(x - 1), math.e)
	print("x | n | F(x) | Math F(x) | eps")
	print(f"{x} | {n} | {f} | {math_f} | {math.fabs(f - math_f)}")
	print(f"average: {statistics.mean(arr)}")
	print(f"median: {statistics.median(arr)}")
	print(f"mode: {statistics.mode(arr)}")
	print(f"variance: {statistics.variance(arr)}")
	print(f"standard deviation: {statistics.stdev(arr)}")
	
	x = numpy.arange(1.05, 2, 0.05)
	y1 = [calculate_taylor(xi, n) for xi in x]
	y2 = [math.log((xi + 1)/(xi - 1), math.e) for xi in x]
	save_graph("task3_directory/graph.png", x, y1, x, y2)
