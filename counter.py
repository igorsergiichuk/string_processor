# the simple instrument to count the number of the words and letters in the text

import string

loop_value = 0
while loop_value == 0:  # Opening loop
    file_path = raw_input("Please, enter the name of the file you want to open: ")
    try:
        file_to_open = open(file_path)
        loop_value = 1
    except:
        print "Please, enter the correct name of the file"

read_file = file_to_open.read()
letter_dict = dict()

alphabet = '''
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
'''
for line in read_file:
    words = line.lower().translate(None, string.punctuation).split()
    for word in words:
        for letter in word:
            if letter not in alphabet: continue
            else: letter_dict[letter] = letter_dict.get(word,0) + 1
sum_of_keys = 0
for val, key in letter_dict.items():
    sum_of_keys = sum_of_keys + key
lst = list()
for val, key in letter_dict.items():
    lst.append((val, (key*100)/float(sum_of_keys)))
lst.sort()
for key, val in lst[:]:
    print "The number of the percents of the letter", key, "in the text is:", val

read_file = read_file.rstrip().split()
amount = len(read_file)
words_dict = dict()
for words in read_file:
    if words not in words_dict:
        words_dict[words] =1
    else: words_dict[words] = words_dict[words] + 1
count = sum(words_dict.values())
if count - amount == 0:
    print ""
    print "The total number of the words in text is: ", count
    print ""
print "The total number of letters in the text is: ", sum_of_keys

