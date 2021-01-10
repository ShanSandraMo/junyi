#Question 2

def reverse_sentence(input_sentence):

	word_list = input_sentence.split()
	reversed_words = []
	
	for item in word_list:
		reversed_item = item[::-1]
		reversed_words.append(reversed_item)
	
	for item in reversed_words:
		new_sentence = ' '.join(reversed.words)
	
	return new_sentence

assert reverse_letters('reverse this sentence') == 'esrever siht ecnetnes'
assert isinstance(reverse_letters('reverse this sentence'), str) 
