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

print(list_dictionary)

result = list_dictionary.OrderedDict(sorted(list_dictionary.items()))

print(result)


'''
list_data = []
sample.split(" ")
for i in sample:
    list_data.append(i)
print(list_data)


def search_element(list_, character):
    counter = 0
    for i in list_:
        if i == character:
            counter += 1
            return counter


print(search_element(list_data, 'a'))

##Q2: Giving two words please provide a list in alphabetical order of common characters found in both words, please avoid using nested loops
##Sample input:
##word_1 = 'maria'
##word_2 = 'marcela'

# The sample output would be:
# ['a', 'm', 'r']
'''
