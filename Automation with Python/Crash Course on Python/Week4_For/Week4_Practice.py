# String Formatting
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print(f"Base price: ${price:.2f}. With Tax ${with_tax:.2f}")


# String Formatting
def to_celsius(cel):
    return (cel - 32) * (5 / 9)


for cel in range(0, 101, 10):
    print(f"{cel:>3} f | {to_celsius(cel):>6.2f} C.")

item = "Purple Cup"
amount = 5
price = amount * 3.25
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')

# String Formatting """
x = ['Now', 'we', 'are', 'cooking!']
print(type(x))
print(x)
print(len(x))
print("are" in (x))
print((x)[0])
print((x)[2])
print((x)[1:3])


# Tuplas
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds((5000))
print(result)
print(type(result))

hours, minutes, seconds = result
print(hours, minutes, seconds)

# Practice tuplas y list
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0

for animal in animals:
    chars += len(animal)
print(f'Total characters: {chars}, average length: {chars / len(animals)}')

# example  tuplas y list
winners = ['Ashley', 'Dylan', 'Reese']
for index, person in enumerate(winners):
    print(f'{index + 1} - {person}')

# Comprehension List
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

multiples = [x * 8 for x in range(1, 11)]
print(multiples)

z = [x for x in range(1, 101) if x % 6 == 0]
print(z)

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filename.replace("hpp", "h") for filename in filenames]
print(newfilenames)

