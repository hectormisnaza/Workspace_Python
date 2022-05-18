price = 7.5
with_tax = price * 1.09
print(price, with_tax)

print(f"Base price: ${price:.2f}. With Tax ${with_tax:.2f}")


""" String Formatting """


def to_celsius(cel):
    return(cel - 32) * (5 / 9)


for cel in range(0, 101, 10):
    print(f"{cel:>3} f | {to_celsius(cel):>6.2f} C.")


""" String Formatting """

item = "Purple Cup"
amount = 5
price = amount * 3.25

print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')

