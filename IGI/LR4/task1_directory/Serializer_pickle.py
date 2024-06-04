from .Serializer_abstract import Serializer
import pickle


class PickleSerializer(Serializer):
	@classmethod
	def serialize(cls, all_synonyms: dict[str,str], path: str):
		try:
			with open(path, mode='wb') as file:
				pickle.dump(all_synonyms, file)
		except:
			print("There was a problem with the serialisation of the object.")


	@classmethod
	def deserialize(cls, path: str):
		all_synonyms = {}
		try:
			with open(path, mode='rb') as file:
				all_synonyms = pickle.load(file)
		except:
			print("There was a problem with the deserialisation of the object.")
		return all_synonyms