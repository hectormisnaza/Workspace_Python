while True:
    try:
        edad = int(input("Escribe tu edad: "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    if edad < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break


int(input("How many values do you want to enter? here =>"))