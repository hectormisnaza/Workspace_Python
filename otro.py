file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

print(file_counts["txt"])

file_counts["cfg"] = 8
print(file_counts)

file_counts["csv"] = 17
print(file_counts)
print(type(file_counts))


def guest_list(guests: object) -> object:
    for guest in guests:
        name, age, job = guest
        print(f"{name} is {age} years old an works as {job}")
        print(type(guest))
        print(type(guests))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
#pytest
