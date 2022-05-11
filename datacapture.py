class data_capt:

    def add(list1):
        for value in range(6):
            try:
                user_input = int(input(value))
            except ValueError:
                print("the value entered is not a number")
            else:
                print(f"{value} {user_input}")
                list1.append(user_input)
        print(f"your number list : ", list1)

    def less(list1, list2, capture):
        dato1 = int(input(f"{txt_3}"))
        print(f"{txt_1}  {dato1}")
        for valor in list1:
            if int(valor) < int(dato1):
                list2.append(valor)
        print(f"{txt_2} {dato1} :", list2)
        return list2

    def greater(list1, list2, capture):
        dato1 = int(input(f"{txt_3}"))
        print(f"{txt_1}  {dato1}")
        for valor in list1:
            if int(valor) > int(dato1):
                list2.append(valor)
        print(f"{txt_2} {dato1} :", list2)

    def between(list1, list2, capture):
        print("recuerde para esta operacion el primer digito debe ser menor al segundo digito que ingrese!")
        dato1 = int(input(f"{txt_0}"))
        dato2 = int(input(f"{txt_0}"))
        print(f"{txt_1}  {dato1}   el segundo valor ingresado es   {dato2}")
        for valor in list1:
            if int(valor) > int(dato1) and int(valor) < int(dato2):
                list2.append(valor)
        print(f"los numeros que estan entre {dato1} y {dato2} son: ", list2)