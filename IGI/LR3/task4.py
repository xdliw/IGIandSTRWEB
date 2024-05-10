

def task4():
	"""
		Function to perform task 4.

		We find all words and output their amount
		the longest word and its position
		and every odd posiotioned word
	"""
	
	
	text = "So she was considering in her own mind,\
		as well as she could, for the hot day made her feel very sleepy and stupid,\
			whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies,\
				when suddenly a White Rabbit with pink eyes ran close by her."

	words = text.replace(',','').replace('.','').split()
	
	max_len = 0 
	max_pos = 0
	for i, word in enumerate(words):
		if len(word) > max_len:
			max_len = len(word)
			max_pos = i + 1 #1-indexed position

	print(f"a) {len(words)}")
	print(f"b) {words[max_pos - 1]} {max_pos}")
	print(f"c) {words[::2]}")

	