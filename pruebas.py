friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print('Hi ', friend)


color = "Green"
thing = "Hope"
print(color + " is the color of " + thing)

semana = 7
dia = 24
minutos = 60
segundos = 60
print(semana * dia * minutos * segundos)

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / disk_size

print(sector_amount)

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")
month_days("June", 30)
month_days("July", 31)

def rectangle_area (base, height):
	z = base*height  # the area is base*height
	print("The area is " + str(z))

rectangle_area(5,6)

# --------------------------------------------------------------
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))
# --------------------------------------------------------------
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
# --------------------------------------------------------------
def lucky_number(name):
	number = len(name) * 9
	message = "Hello " + name + ". Your lucky number is " + str(number)
	return message

print(lucky_number("Kay"))
print(lucky_number("Cameron"))
# --------------------------------------------------------------
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
# --------------------------------------------------------------
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
# --------------------------------------------------------------
number = 10

if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
# --------------------------------------------------------------
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * full_blocks + block_size
    return block_size*full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
# --------------------------------------------------------------
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("red")) # Should be #ff0000
print(color_translator("green")) # Should be #00ff00
print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("black")) # Should be unknown
print(color_translator("")) # Should be unknown
# --------------------------------------------------------------
def format_name(first_name, last_name):
	if first_name != "" and last_name != "":
		string = ("Name: " + first_name + ", " + last_name)
		return string
	elif first_name != '' or last_name != '':
		string = ("Name: " + last_name + first_name)
		return string
	else:
		string = ""
	return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
# --------------------------------------------------------------
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)
print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
# --------------------------------------------------------------
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
	if denominator != 0:
		return (numerator/denominator)%1
# keep just the fractional part of the quotient
	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
