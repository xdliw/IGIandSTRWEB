from Serializer_csv import CsvSerializer
from Serializer_pickle import PickleSerializer
from Serializer_abstract import Serializer
from ..tools.tools import conditional_input
from pprint import pprint


class task1_Class:
	@staticmethod
	def Execute():
		all_synonyms = {
			"Black" : "White",
			'Cat' : "Dog",
			"Car" : "Airplane"
		}
		choice = conditional_input(int, lambda x: 1 <= x <= 2, "Enter the serialisation method (1 - csv, 2 - pickle): ")
		serializer: Serializer
		match choice:
			case 1:
				path = "task1/task1.csv"
				serializer = CsvSerializer
			case 2:
				path = "task1/task1.pickle"
				serializer = PickleSerializer

		serializer.serialize(all_synonyms, path)
		loaded_synonyms = serializer.deserialize(path)
		print("All synonyms")
		pprint(loaded_synonyms)
		word = input("Enter word to get synonym for it if its in the dict: ")
		print("Synonym:", loaded_synonyms[word])
