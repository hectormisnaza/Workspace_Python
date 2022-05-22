##Q1: Giving the following string

sample = "aaabbbccbacdeb"
##Print the 3 most common characters along with their occurrence count each on a separate line.
##Sort output in descending order of occurrence count.
##Note: order by letter if the number repeats
##The sample output would be:
##b : 5
##a : 4
##c : 3
list_dictionary = {}
for val in sample:
    if not list_dictionary.get(val):
        list_dictionary[val] = 1
    else:
        list_dictionary[val] += 1

sorted_list_dic = sorted(list_dictionary.items(), key=lambda x: x[1], reverse=True)
print(list_dictionary)
print(sorted_list_dic)

""" Q2: Giving two words please provide a list in alphabetical order of common characters found in both words, please 
avoid using nested loops """

# Sample input:
word_1 = 'maria'
word_2 = 'marcela'
list_1=[]

def string_val(val1, val2):
    for a in val1:
        for b in val2:
            if a == b:
                if not a in list_1:
                    list_1.append(a)
                    list_1.sort()
    return list_1

print(string_val(word_1, word_2))
# The sample output would be:
# ['a', 'm', 'r']
