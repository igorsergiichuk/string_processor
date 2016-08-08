import string

loop_value = 0
while loop_value == 0:  # Opening loop
    file_path = raw_input("Please, enter the name of the file you want to open: ")
    try:
        file_to_open = open(file_path)
        loop_value = 1
    except:
        print "Please, enter the correct name of the file"


def pop_out(list_of_items):  # Remove duplicating items in list
    original = list(set(list_of_items))
    return original


def del_punct(string_st):  # Delete punctuation from list
    punk = string.punctuation
    joiner = ""
    new_l = []
    for item in string_st:
        for letter in item:
            if letter == " " or item not in punk:
                new_l.append(letter)
                string_fin = joiner.join(new_l)
    return string_fin


def del_digits(list_of_items):  # Delete digits form list
    digits = string.digits
    new_l = []
    for item in list_of_items:
        for digit in item:
            if digit in digits:
                new_l.append(list_of_items.index(item))
                cleaned = pop_out(new_l)
                cleaned.reverse()
    for ind in cleaned:
            list_of_items.pop(ind)
    return list_of_items

read_file = file_to_open.read()
cleaned_file = del_punct(read_file)
list_file = cleaned_file.strip().split()

list_of_words = []
for word in list_file:
     list_of_words.append(word.lower())

no_dublic = pop_out(list_of_words)
no_dublic.sort()

finish = del_digits(no_dublic)
print finish
