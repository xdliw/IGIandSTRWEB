from .figure_color import Figure_color
from .geometric_figure import Geometric_figure
from math import sqrt
from .nameMixin import NameMixin

class Regular_triangle(NameMixin, Geometric_figure):

	#methods
	def __init__(self, side_length : float, color : str, name : str):
		super().__init__(name)
		self.__side_length = side_length
		self.__color = Figure_color(color)

	def get_area(self):
		return self.__side_length ** 2 * sqrt(3) / 2
	
	@property
	def color(self):
		return self.__color
	
	def __str__(self):
		return "side length is {}, color is {}".format(self.__side_length, self.__color.value)
	
	