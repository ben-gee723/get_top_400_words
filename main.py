# Imports
import re
import requests
from collections import defaultdict, Counter
from itertools import islice
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

# Counter
# Count the words in a string and

testStr1 = "!This is $a   simple string."
testStr2 = "The the the"
longTest = "The Python TypeError: unhashable type: 'list' usually means that a list is being used as a hash argument. This error occurs when trying to hash a list, which is an unhashable object. For example, using a list as a key in a Python dictionary will cause this error since dictionaries only accept hashable data types as a key."
url = 'https://en.wikipedia.org/wiki/English_Wikipedia'

filename = '../../../../Dokumente/enwiki-20220101-pages-articles-multistream/enwiki-20220101-pages-articles-multistream.xml'

unwanted_strings = ['en', 'mw', 'hlist', 'dd', 'dt', 'li', 'cs1', 'ext']

# 1. GET - Raw text from a website
def get_str_text_from_html(url):
	content = requests.get(url)
	soup = BeautifulSoup(content.text, 'html.parser')
	return soup.get_text()

# 2. FILTER - Go through string and filter out symbols & extra spaces. return list of strings
def filter_str_to_array(str):
	print(str)
	list_with_empty_strs = re.sub(r'[^\w]', ' ', str).strip().lower().split(' ')
	return [x for x in list_with_empty_strs if not x.isdigit() and x != '' and len(x) != 1 and x not in unwanted_strings]



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

# 6. GET TOP WORDS

# main Funktion
def main(filename): 
	parser = ET.iterparse(filename)
#	print(parser)
	for event, element in parser:
		print(element.tag)
#	string = get_str_text_from_html(url)
#	print(string)
		list_of_strs = filter_str_to_array(element.text)
#	print(list_of_strs)
		words_count = count_words(list_of_strs)
		ordered_words_counts = order_to_highest_count(words_count)
#	print(ordered_words_counts)
		top_words =  top_words_by_number(ordered_words_counts, 50)
	return top_words
	element.clear()
#	print(top_words)


# run main
if __name__ == "__main__":
	main(filename) 