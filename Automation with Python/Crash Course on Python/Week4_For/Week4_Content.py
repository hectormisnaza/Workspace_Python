"""
Modify the double_word function so that it returns the same word repeated twice,
followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.
"""


def double_word(word):
    word *= 2
    count = 0
    for letter in word:
        count += 1
    return word + str(count)


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0
# The Parts of a String
"""Modify the first_and_last function so that it returns True if the first letter of the string is the same as the 
last letter of the string, False if they’re different. Remember that you can access characters using message[0] or 
message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing. """


def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Creating New Strings
""" Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious". """

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

# More String Methods
"""Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase 
received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return 
"LAN”. """


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS

# Formatting Strings
"""Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the 
exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam". """


def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# Lists
# What is a list?
"""The group_list function accepts a group name and a list of members, and returns a string with the format: 
group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in 
this function to do that. """


def group_list(group, users):
    members = group + ": " + ", ".join(users)
    return members


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"

# Modifying the Contents of a List
"""The skip_elements function returns every other element from the list, starting from the first. Complete this 
function to do that."""


def skip_elements(elements):
    new_elements = []
    for element in elements:
        if elements.index(element) % 2 == 0:
            new_elements.append(element)
    return new_elements


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []

"""Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word 
from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 
4th word in this sentence. Hint: remember that list indexes start at 0, not 1. """


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]
    return ""


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

"""The skip_elements function returns a list containing every other element from an input list, starting with the 
first element. Complete this function to do that, using the for loop to iterate through the input list. """


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for elem in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_list.append(elem)
        # Increment i
        i += 1

    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []

# Lists and Tuples
"""The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, 
and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, 
"Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. 
Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this 
function to do that. """


def guest_list(guests):
    for guest in guests:
        name, age, job = guest
        print("{} is {} years old and works as {}".format(name, age, job))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Iterating over Lists and Tuples
"""Complete the skip_elements function to return every other element from the list, this time using the enumerate 
function to check if an element is on an even position or an odd position. """


def skip_elements_enumerate(elements):
    new_elements = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_elements.append(element)
    return new_elements


print(skip_elements_enumerate(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements_enumerate(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

# Tuplas
"""Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in 
this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. """


def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}".format(size / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21

# List Comprehension
"""The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the 
function, using ListComprehension. Hint:remember that list and range counters start at 0 and end at the limit minus 1"""


def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []

"""Complete the skip_elements function to return every other element from the list, this time using a list 
comprehension to generate the new list based on the previous one, where elements in odd positions are skipped. """


def skip_elements_list_comprehension(elements):
    return [element for element in elements if elements.index(element) % 2 == 0]


print(skip_elements_list_comprehension(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements_list_comprehension(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

# Dictionaries
# What is a dictionary?
"""The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) Add 
an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3) Display the new dictionary 
contents. 4) Display True if there is Chapter 5, False if there isn't. """

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print (toc) # What are the current contents of the dictionary?
print ("chapter 5" in toc)     # Is there a Chapter 5?

# Iterating over the Contents of a Dictionary
"""Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items 
method returns a tuple of key, value for each element in the dictionary. """

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, feature in cool_beasts.items():
    print("{} have {}".format(beast, feature))

# Dictionaries vs. Lists
"""In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be 
a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their 
colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", 
"blue shirt", and so on. """

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for cloth in wardrobe:
    for color in wardrobe[cloth]:
        print("{} {}".format(color, cloth))
