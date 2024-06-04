import re

class Solution_regexes:
	@staticmethod
	def count_interrogative_sentences(text : str) -> int:
		return len(re.findall(r'\?', text))
	
	@staticmethod
	def count_exclamatory_sentences(text : str) -> int:
		return len(re.findall(r'!', text))
	
	@staticmethod
	def count_narrative_sentences(text : str) -> int:
		return len(re.findall(r'\.', text))
	
	@staticmethod
	def count_all_sentences(text : str) -> int:
		return\
			Solution_regexes.count_interrogative_sentences(text) +\
			  Solution_regexes.count_exclamatory_sentences(text) +\
					Solution_regexes.count_narrative_sentences(text)
	
	@staticmethod
	def count_average_sentence_length(text : str):
		'''in symbols that are in words'''

		symbols = re.findall(r"\w", text)
		number_of_sentences = Solution_regexes.count_all_sentences(text)
		

		#There were no specifications to handling exceptions, so i did that.
		try:
			result = len(symbols) / number_of_sentences
		except ZeroDivisionError:
			result = "No sentences"

		return result
	
	@staticmethod
	def count_average_word_length(text : str):
		'''in symbols that are in words'''

		symbols = re.findall(r"\w", text)
		words = re.findall(r"\w+", text)


		#There were no specifications to handling exceptions, so i did that.
		try:
			result = len(symbols) / len(words)
		except:
			result = "No words"

		return result
	
	@staticmethod
	def count_smileys(text : str):

		return len(re.findall(r"[;:]-*([()\[\]])\1*", text))
	
	@staticmethod
	def get_all_specific_words(text : str):
		'''words that include a symbol from a-o or 0-9'''

		return re.findall(r"\b\w*[a-o\d]\w*\b", text)
	
	def is_string_sixdigit_decimal(number : str):

		result = bool(re.match(r"\b(?!0)\d{6}\b", number))
		return result
	
	def count_words_in_quotes(text : str):
		'''quotes: " '''
		
		strings_inside_quotes = re.findall(r'"(?:\n|.)+?"', text)

		result = 0
		for string in strings_inside_quotes:
			result += len(re.findall(r"\w+", string))

		return result
		
	def count_all_letters_occurences(text : str):
		'''for a-z and A-Z'''

		result = {}

		for char in range(ord('a'), ord('z') + 1):
			letter = chr(char)
			result[letter] = len(re.findall(fr"{letter}", text))

		for char in range(ord('A'), ord('Z') + 1):
			letter = chr(char)
			result[letter] = len(re.findall(fr"{letter}", text))

		return result
	
	def get_all_comma_collocations(text : str):
		'''collocations that are: (word , word)'''

		result = re.findall(r"\w+\s*,\s*\w+", text)

		return result
