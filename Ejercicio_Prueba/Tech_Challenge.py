while True:
    print("\n Welcome, we will perform basic operations  \n 1) I want to do an operation.  \n 2) exit")
    opcion = input("Select 1 or 2. here =>")
    if opcion == "1":
        list1 = []
        list2 = []
        cdatos = ""

        def add(list1):
            global cdatos
            while True:
                try:
                    cdatos = int(input("How many values do you want to enter? here =>"))
                except ValueError:
                    print("the value entered is not a number")
                    continue
                if cdatos < 0:
                    print("the value entered is not a number")
                    continue
                else:
                    break
            print(f"the value entered {cdatos}  values")
            for value in range(cdatos):
                try:
                    user_input = int(input(txt_0))
                except ValueError:
                    print("the value entered is not a number")
                else:
                    print(f"{txt_1} {user_input}")
                    list1.append(user_input)
            print(f"your number list : ", list1)

        def less(list1, list2):
            dato1 = int(input(f"{txt_3}  {capture} here=>"))
            print(f"{txt_1}  {dato1}")
            for valor in list1:
                if int(valor) < int(dato1):
                    list2.append(valor)
            print(f"{txt_2} {capture} {dato1} :", list2)
            return list2


        def greater(list1, list2):
            dato1 = int(input(f"{txt_3}  {capture} here=>"))
            print(f"{txt_1}  {dato1}")
            for valor in list1:
                if int(valor) > int(dato1):
                    list2.append(valor)
            print(f"{txt_2} {capture} {dato1} :", list2)


        def between(list1, list2):
            print("The first digit must be less than the second digit!")
            dato1 = int(input(f"{txt_0}"))
            dato2 = int(input(f"{txt_0}"))
            print(f"{txt_1}  {dato1}   el segundo valor ingresado es   {dato2}")
            for valor in list1:
                if int(dato1) < int(valor) < int(dato2):
                    list2.append(valor)
            print(f"the numbers that are between {dato1} and {dato2} are: ", list2)

        print("we will create a list, with the list we execute basic statistics ")

        txt_0 = " enter value number, here =>"
        txt_1 = " entered value: "
        txt_2 = " The following numbers are"
        txt_3 = " enter your number for basic statistics "

        add(list1)

        capture = input(
            'what operation do you want to perform? insert: '
            '\n"less" to find the less numbers   '
            '\n"greater" to find the grater numbers  '
            '\n or "between" to know the numbers between two digits. \n here =>')

        if capture == 'less':
            less(list1, list2)
        elif capture == 'greater':
            greater(list1, list2)
        elif capture == 'between':
            between(list1, list2)
        else:
            print(
                f"The entered value: {capture} It is not 'less', 'greater' o 'between'. ")
    elif opcion == "2":
        print()
        break
    else:
        print("The number entered is wrong")
