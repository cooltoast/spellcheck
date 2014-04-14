from bisect import bisect_left

with open("/usr/share/dict/words") as dictionary:
  library = dictionary.read().lower().splitlines()
print "Dictionary initialized with length", len(library)

#returns index of x in a_list, assuming a_list is sorted
def binary_search(a_list, x, lo=0, hi=None):
  hi = hi if hi is not None else len(a_list)    
  pos = bisect_left(a_list,x,lo,hi)          
  return (pos if pos != hi and a_list[pos] == x else -1)


def remove_duplicates (library):
  checked_list = []
  for word in library:
    if (word not in checked_list):
      checked_list.append(word)
  return checked_list

#checks for duplicates and removes them and replaces all vowels with 'a'
def duplicates(w, v):
  import itertools
  import re
  #duplicates
  noDup = ''.join(ch for ch, _ in itertools.groupby(w))
  #vowels
  allNew = re.sub("[aeiou]", "a", noDup)
  return allNew

#O(n^2), but necessary to make lookup time 
#O(log(n)) for binary search
def clear_duplicates_and_sort(a_list):
  
  for word in library:
    if (library.count(word) > 1):
      library.remove(word)
      
  a_list.sort()    
  return a_list  

#~~~~~~method below finds index of word in dictionary list~~~~~
#~~~~~~work toward spell suggestions~~~~~~~~~~~~~~~~~~~~~

alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = ('aeiou')
prompt = 'Enter a word: '

#no upper case words
word = raw_input(prompt).lower()
print word

index = binary_search(library, word)

print "word appears: ", library.count(word)

print "prev word: ", library[index - 1]
print "word: ", library[index]
print "next word: ", library[index + 1]

print "prev word: ", library[library.index(word) - 1]
print "word: ", library[library.index(word)]
print "next word: ", library[library.index(word) + 1]

print "removing duplicates..."

library = clear_duplicates_and_sort(library)
#library = remove_duplicates(library)


print "word appears: ", library.count(word)

index = binary_search(library, word)

print "prev word: ", library[index - 1]
print "word: ", library[index]
print "next word: ", library[index + 1]

print "prev word: ", library[library.index(word) - 1]
print "word: ", library[library.index(word)]
print "next word: ", library[library.index(word) + 1]



'''
print "index is: ", index
print "index is: ", library.index(word)
'''
#assert binary search works
#Python index function is O(n)
#Binary search is O(log(n))
#reference: https://wiki.python.org/moin/TimeComplexity
if (index == library.index(word)):
	print "It worked!"

#~~~~~~method above finds index of word in dictionary list~~~~~
#~~~~~~work toward spell suggestions~~~~~~~~~~~~~~~~~~~~~

#gets new word with no duplicates/replaced vowels
newWord = duplicates(word, "aeiou")

#searches for new word in dictionary + calculates Lev + provides suggestion
new_index = binary_search(library, newWord)
print newWord


newWord = duplicates(newWord, "aeiou")


print newWord

for letter in newWord:
  if (letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
    print "duplicates failed"

'''
a_list = [0,1,2,3,4,5,6,7,8,9]
#binary_search test
print binary_search(a_list, 5)
'''


"""
keeps /n

dictionary = open("/usr/share/dict/words")
library = dictionary.readlines()
"""




'''
#set up trie data structure
class trieStruc:
	def __init__(self):
		self.word = None
		self.children = {}

		def insert(self,word):
			element = self
			for letter in word:
				if letter not in self.children:
					self.children[letter] = trieStruc()

				element = self.children[letter]

			element.word = word

#fill trie with words from dictionary			
trie = trieStruc()
for one in library:
	trie.insert(one)						

print trie
'''
'''
#checks for duplicates and removes them and replaces all vowels with 'a'
def duplicates(w, v):
	import itertools
	import re
	#duplicates
	noDup = ''.join(ch for ch, _ in itertools.groupby(w))
	#vowels
	allNew = re.sub("[aeiou]", "a", noDup)
	return allNew


#binary search for words without any duplicates and vowels replaced with 'a'
def binarySearch():
    global found, lower, upper, midpoint
    lower = 0
    upper = len(library)-1
    found = False
    while lower <= upper and not found:
        midpoint = (lower + upper) / 2
        print "M: ", midpoint
        print "U: ", upper
        print "L: ", lower
        if library[midpoint] < newWord:
            lower = midpoint+1
        elif library[midpoint] > newWord:
            upper = midpoint-1
        else:
            found = True

    if found:
        print "Found it at", midpoint
    else:
		print "NO SUGGESTION"

#gets new word with no duplicates/replaced vowels
newWord = duplicates(word, "aeiou")

#searches for new word in dictionary + calculates Lev + provides suggestion
binarySearch()
print newWord
'''