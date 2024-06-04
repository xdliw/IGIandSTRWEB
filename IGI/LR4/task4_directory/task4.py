if __name__ == "__main__":
	import os
	import sys

	sys.path.append(os.path.dirname(__file__) + "/..")

from task4_directory.regular_triangle import Regular_triangle
from task4_directory.square import Square
from tools.tools import conditional_input as cin
import matplotlib.pyplot as plt
import math

def task4():
	
	side = cin(float, lambda x : x > 0, "input positive side length for square and triangle: ")
	label = cin(str, None, "input label for the figures: ")

	colors = {'r', 'b', 'c', 'g', 'm', 'y', 'k'}
	print("Acceptable colors:", colors)
	color = cin(str, lambda x: x in colors, "Enter a color: ")
	
	
	square = Square(side, color, "Square")
	triangle = Regular_triangle(side, color,"Regular triangle")


	print(square.get_name())
	print(str(square))
	print(triangle.get_name())
	print(str(triangle))

	#square
	x = [1, 1 + side, 1 + side, 1, 1]
	y = [1, 1, 1 + side, 1 + side, 1]
	plt.plot(x, y, label = label, color = square.color.value)
	plt.fill(x, y, color = square.color.value)
	plt.legend()

	#triangle
	h = side * math.sqrt(3) / 2
	x = [1, 1 + side / 2, 1 + side]
	y = [1 + side, 1 + side + h, 1 + side]
	plt.plot(x, y, label = label, color = triangle.color.value)
	plt.fill(x, y, color = triangle.color.value)
	
	plt.axis('equal')
	plt.legend()
	path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task4_directory/graph.png'
	plt.savefig(path)
	plt.show()



if __name__ == "__main__":
	task4()