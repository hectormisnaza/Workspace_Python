import datacapture
list1 = []
list2 = []

capture = input ("que operacion quieres realizar? escribe: \n'less' para encontrar los numeros menores que, \n'greater' para encontrar los numeros mayores que \n o 'between' para saber cuales son los numeros que se encuentran entre dos digitos. \n escriba aqui=>")

txt_0 = (" enter value number, here =>")
txt_1 = (" value: ")
txt_2 = (f" The following numbers are {capture} than ")
txt_3 = (f" enter your number for basic statistics, here => ")

print("crearemos un listado de 6 valores en el cual se realizara basic statistics ")

add()

if capture == 'less':
    less(list1,list2, capture, txt_1, txt_2, txt_3)
elif capture == 'greater':
    greater(list1,list2, capture, txt_1, txt_2, txt_3)
elif capture == 'between':
    between(list1,list2, capture, txt_1, txt_2, txt_3)
else:
    print(f"el valor ingresado {capture} no corresponde a 'less', 'greater' o 'between' segun las instrucciones")