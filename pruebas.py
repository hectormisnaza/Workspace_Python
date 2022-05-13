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

disk_size = 16 * 1024 * 1024 * 1024
sector_size = 512
sector_amount = disk_size / disk_size

print(sector_amount)

# --------------------------------------------------------------

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")


month_days("June", 30)
month_days("July", 31)

# --------------------------------------------------------------

def rectangle_area(base, height):
    z = base * height  # the area is base*height
    print("The area is " + str(z))

rectangle_area(5, 6)

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
print("The round-trip in kilometers is " + str(my_trip_km * 2))


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


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative


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
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * full_blocks + block_size
    return block_size * full_blocks


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192


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


print(color_translator("red"))  # Should be #ff0000
print(color_translator("green"))  # Should be #00ff00
print(color_translator("blue"))  # Should be #0000ff
print(color_translator("yellow"))  # Should be unknown
print(color_translator("black"))  # Should be unknown
print(color_translator(""))  # Should be unknown


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
    return (word)


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


# --------------------------------------------------------------
def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    if denominator != 0:
        return (numerator / denominator) % 1
    # keep just the fractional part of the quotient
    return 0


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0
# --------------------------------------------------------------
x = 0
while x < 5:
    print ("Not there yet, x=" + str(x))
    x = x +1
print ("x=" + str(x))
# --------------------------------------------------------------
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)
# --------------------------------------------------------------
def count_down(current):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")
count_down(3)
# --------------------------------------------------------------
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
# --------------------------------------------------------------
def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    if n == 0:
        return False
    while n % 2 == 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False

print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False
# --------------------------------------------------------------
def sum_divisors(n):
# Return the sum of all divisors of n, not including n
  i = 1
  sum = 0
  while i < n :
    if n % i == 0:
      sum +=  i
      i += 1
    else:
      i += 1
  return sum

print(sum_divisors(0))  # 0
print(sum_divisors(3)) # Should sum of 1   # 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18  # 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51    # 114
# --------------------------------------------------------------
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3)   # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5)    # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)	    # Should print: 8x1=8 8x2=16 8x3=24
# --------------------------------------------------------------
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range (x):
        sum += square (n)
    return sum

print(sum_squares(10)) # Should be 285
# --------------------------------------------------------------
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
# --------------------------------------------------------------
def to_celsius(x):
    return (x - 32) * 5 / 9
for x in range (0, 100, 10):
    print (x, to_celsius(x))
# --------------------------------------------------------------
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
# --------------------------------------------------------------
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print (home_team + " vs "+ away_team)
# --------------------------------------------------------------
def greet_friends(friends):
    for friend in friends:
        print ("hi " + friend)
greet_friends(['Taylor', 'Luisa', 'Jammal', 'Eli'])
greet_friends('Barry')
greet_friends(['Barry'])
# --------------------------------------------------------------
def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")
validate_users(["purplecat"])
# --------------------------------------------------------------
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result
for n in range(1,10):
    print(n, factorial(n))
# --------------------------------------------------------------
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(1,10):
    print(n, factorial(n))
# --------------------------------------------------------------
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)
# --------------------------------------------------------------
def factorial(n):
  if n < 2:
    print ("returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result)+" for factorial of "+ str(n))
  return result

factorial (5)
# --------------------------------------------------------------
def sum_positive_numbers(n):
  # The base case is n being smaller than 1
  if n < 1:
    return n
  # The recursive case is adding this number to
  # the sum of the numbers smaller than this one.
  return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15
# --------------------------------------------------------------
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number==1
  result = number//base

  # Recursive case: keep dividing number by base.
  return is_power_of(result, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
# --------------------------------------------------------------
def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member) -1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
# --------------------------------------------------------------
def sum_positive_numbers(n):
  result = 0
  for x in range (n+1):
    result += x
  return result

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
# --------------------------------------------------------------
def sum_positive_numbers(n):
  if n <= 1:
    return n
  return n + sum_positive_numbers (n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
