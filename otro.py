def factorial(n):
    result = 0
    for x in range(1, n +1):
        result = result + x
    return result


for n in range(1,5):
    print(n, factorial(n))