# Imports
import re
from collections import defaultdict, Counter
from itertools import islice


# Counter
# Count the words in a string and

testStr1 = "!This is $a   simple string."
testStr2 = "The the the"
longTest = "The Python TypeError: unhashable type: 'list' usually means that a list is being used as a hash argument. This error occurs when trying to hash a list, which is an unhashable object. For example, using a list as a key in a Python dictionary will cause this error since dictionaries only accept hashable data types as a key."

# 1. GET - Raw text from a website


# 2. FILTER - Go through string and filter out symbols & extra spaces. return list of strings
def filter_str_to_array(str):
	list_with_empty_strs = re.sub(r'[^\w]', ' ', str).strip().lower().split(' ')
	return [x for x in list_with_empty_strs if x != ''];



# 3. COUNT - Loop through string words and count each word. Save word as Tuple(?) and append to list(?)
def count_words (list_of_strs):
	words = defaultdict(list)
	for newWord in list_of_strs:
		if words.get(newWord) is not None:
			words[newWord] = words[newWord] + 1
		else:
			words[newWord] = 1
	return words


# 4. ORDER - Words ordered
def order_to_highest_count(words_list): 
	return {k: v for k, v in sorted(words_list.items(), key=lambda item: item[1], reverse=True)}


# 5. TOP WORDS
def top_words_by_number(words_list, number = 10): 
	top_words = list(islice(words_list, number))
	for num, word in enumerate(top_words, start=1):
		print(f'{num}: {word}')
	return top_words



# main Funktion
def main(string): 
	list_of_strs = filter_str_to_array(string)
	words_count = count_words(list_of_strs)
	ordered_words_counts = order_to_highest_count(words_count)
	print(ordered_words_counts)
	top_words =  top_words_by_number(ordered_words_counts, 20)
	print(top_words)


# run main
if __name__ == "__main__":
	main(longTest) 