"""The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read
from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are
words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True
if the passed string is a palindrome, False if not. """


def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if letter != " ":
            new_string += letter.lower()
            reverse_string = letter.lower() + reverse_string
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True

"""Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles 
equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 
19.2 km". """


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km

"""PFill in the gaps in the nametag function so that it uses the format method to return first_name and the 
first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."" """


def nametag(first_name, last_name):
    return "{} {:.1s}.".format(first_name, last_name)


print(nametag("Jane", "Smith"))  # Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))  # Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))  # Should display "Jean-Luc G."

"""The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence 
ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the 
end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, 
not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should 
return abcabc (no changes made). """


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))  # Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells",
                     "donuts"))  # Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))  # Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))  # Should display "The weather is nice in April"


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if old[:] == sentence[-len(old):]:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

# Pactice Quiz: List
"""Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, 
we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the 
code using any of the methods you’ve learned thus far, like a for loop or a list comprehension. """

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = [filename.replace("hpp", "h") for filename in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        filename = filename.replace(".hpp", ".h")
        newfilenames.append(filename)
    else:
        newfilenames.append(filename)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

"""Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving 
the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay."""


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        text = word[1:] + word[0] + 'ay' + ' '
        say += text
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))
# Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))
# Should be "rogrammingpay niay ythonpay siay unfay"


""" The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute 
for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, 
with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, 
and x or - when the permission is not granted.
 For example: 
 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, 
    it would be: "rw-r-----"
 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, 
    it would be: "rwxr-xr-x"
 Fill in the blanks to make the code convert a permission in octal format into a string format."""


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += '-'
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

"""The group_list function accepts a group name and a list of members, and returns a string with the format: 
group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in 
this function to do that. """


def group_list(group, users):
    members = ", ".join(users)
    return f"{group}: {members}"


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"

"""The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, 
and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, 
"Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. 
Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this 
function to do that. """


def guest_list(guests):
    for guest in guests:
        name, age, job = guest
        print(f"{name} is {age} years old and works as {job}")


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

def guest_list(guests: object) -> object:
    for guest in guests:
        name, age, job = guest
        print(type(guest))
        print(type(guests))
        print(f"{name} is {age} years old an works as {job}")

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
