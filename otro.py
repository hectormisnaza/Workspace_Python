def skip_elements_enumerate(elements):
    new_elements = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_elements.append(element)
    return new_elements


print(skip_elements_enumerate(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements_enumerate(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']