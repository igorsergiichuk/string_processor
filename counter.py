# the simple instrument to count the words in the text

loop_value = 0
while loop_value == 0:  # Opening loop
    file_path = raw_input("Please, enter the name of the file you want to open: ")
    try:
        file_to_open = open(file_path)
        loop_value = 1
    except:
        print "Please, enter the correct name of the file"

read_file = file_to_open.read()
read_file = read_file.rstrip().split()

amount = len(file_to_read)
words_dict = dict()
for words in file_rd:
    if words not in words_dict:
        words_dict[words] =1
    else: words_dict[words] = words_dict[words] + 1
count = sum(words_dict.values())
if count - amount == 0: print count
