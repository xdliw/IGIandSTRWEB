from abc import ABC, abstractmethod

class Geometric_figure(ABC):

	@abstractmethod
	def get_area(self):
		pass