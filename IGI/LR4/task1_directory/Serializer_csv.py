from .Serializer_abstract import Serializer
import csv


class CsvSerializer(Serializer):
	@classmethod
	def serialize(cls, all_synonyms: dict[str,str], path: str):
		try:
			with open(path, mode='w', newline='') as file:
				writer = csv.writer(file)
				writer.writerow(['Word','Synonym'])
				for word, synonym in all_synonyms.items():
						writer.writerow([word, synonym])
		except:
			print("There was a problem with the serialisation of the object.")


	@classmethod
	def deserialize(cls, path: str):
		all_synonyms = {}
		try:
			with open(path, mode='r', newline='') as file:
				reader = csv.reader(file)
				next(reader)
				for row in reader:
					word = row[0]
					synonym = row[1]
					if word in all_synonyms:
						all_synonyms[word].append(synonym)
					else:
						all_synonyms[word] = [synonym]
		except:
			print("There was a problem with the deserialisation of the object.")
		return all_synonyms