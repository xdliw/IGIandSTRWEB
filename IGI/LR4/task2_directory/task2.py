'''
sentences
smileys

11 var:
	numbers
	...

	

input file
output file -> zip

'''

if __name__ == "__main__":
	import os
	import sys
	sys.path.append(os.path.dirname(__file__) + "/..")

from task2_directory.Solution_regexes import Solution_regexes as S

def task2():

	#1)Хорошая ли практика складывать все в лист, а потом '\n'.join и потом записывать в файл?
	#2)В консольном приложении неудобно было бы выбирать файл, я вписал пути тут. А как было по-другому?
	#	в теории можно было бы дать возможность использовать ls и выбрать цифру или ввести название файла в этой директории.
	# есть вариант проще?

	#Пути к файлам с тестами
	output_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/output.txt'
	small_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/small_test.txt'
	text_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/text_test.txt'
	smiley_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/smileys_test.txt'
	combined_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/combined_test.txt'
	number_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/number_test.txt'
	quotes_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/quotes_test.txt'
	letters_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/letters_test.txt'
	comma_collocation_test_file_path = '/home/pessec/prog/4sem/IGI/IGIandSTRWEB/IGI/LR4/task2_directory/tests/comma_collocation_test.txt'


	#Далее, для разных задач открываются файлы с тестами по этим задачам
	with open(output_file_path,'wt') as fout:
	
		result = []

		with open(combined_test_file_path,'rt') as ftest:
			text = ftest.read()
			
			result.append("[GENERAL TASK]")
			result.append(f"[text]:\n{text}")
			result.append(f"[results]:")
			result.append(f"number of interrogative sentences: {S.count_interrogative_sentences(text)}")
			result.append(f"number of exclamatory sentences: {S.count_exclamatory_sentences(text)}")
			result.append(f"number of narrative sentences: {S.count_narrative_sentences(text)}")
			result.append(f"number of sentences: {S.count_all_sentences(text)}")
			result.append(f"average sentence length: {S.count_average_sentence_length(text)}")
			result.append(f"average word length: {S.count_average_word_length(text)}")
			result.append(f"number of smileys: {S.count_smileys(text)}")
			result.append("[SPECIAL TASK]")
			result.append(f"all words that include a-o or 0-9: {S.get_all_specific_words(text)}")
	
		with open(number_test_file_path,'rt') as ftest_number:
			result.append("[number tests]")
			
			for line in ftest_number:
				string = line.rstrip('\n')
				result.append(f"Is string '{string}' a six-digit decimal with no leading zeros: {S.is_string_sixdigit_decimal(string)}")
			
			result.append("[end of number tests]")

		with open(quotes_test_file_path,'rt') as ftest:
			text = ftest.read()
			result.append(f"[quotes test text]:\n{text}")
			result.append(f"number of words in quotes: {S.count_words_in_quotes(text)}")
		
		with open(letters_test_file_path,'rt') as ftest:
			text = ftest.read()
			result.append(f"[letters test text]:\n{text}")
			result.append(f"occurences of letters: {S.count_all_letters_occurences(text)}")
		
		with open(comma_collocation_test_file_path,'rt') as ftest:
			text = ftest.read()	
			result.append(f"[comma collocations test text]:\n{text}")
			result.append(f"all comma collocations sorted: {sorted(S.get_all_comma_collocations(text))}")
			
		result = '\n'.join(result)

		fout.write(result)
		
		print(f"results are printed in output file: {output_file_path}")



if __name__ == "__main__":
	task2()