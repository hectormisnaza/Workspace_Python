from tkinter import *
import random

capture = input ("que operacion quieres realizar? escribe: \n'menor' para encontrar los numeros menores que, \n'mayor' para encontrar los numeros mayores que \n o 'entre' para saber cuales son los numeros que se encuentran entre dos digitos. \n escriba aqui=>")
print(capture)
list1 = random.sample(range(1,20),18)
#list1 = [5,1,4,6,8,9,7,2,6,8,4,1,9,8,4,6,5,3,8,3,1,3]
list2 = []
list3 = []
list4 = []

dato1 = int(input("ingrese in valor numerico"))
dato2 = int(input("ingrese in valor numerico"))
print (f"el valor ingresado es  {dato1} el segundo valor ingresado es {dato2}")


if capture == 'menor':
    for valor in list1:
        if int(valor) < int(dato1):
            list3.append(valor)
    print(f"\nlos numeros menores a {dato1} son: ", list3)
elif capture == 'mayor':
    for valor in list1:
        if int(valor) > int(dato1):
            list2.append(valor)
#print(list2) #(valor, end=",")
    print(f"\nlos numeros mayores a {dato1} son: ", list2)

for valor in list1:
    if int(valor) > int(dato1) and int(valor) < int(dato2):
        list4.append(valor)
print(f"\nlos numeros que estan entre {dato1} y {dato2}son: ", list4)

def hide_b(widget):
    widget.pack_forget()
def show_b(widget):
    widget.pack()

# Vetana
ventana = Tk()

# Etiquetas
etiqueta1 = Label(ventana,text="What would you like to do?")
etiqueta1.grid(row=2,column=3)

# Botones
boton1 = Button(ventana, text="Ingresar Numeros", width=12)
boton1.grid(row=0,column=1)
boton2 = Button(ventana, text="Num aleatorios", width=12)
boton2.grid(row=0,column=3)
boton3 = Button(ventana, text="Mayor o =", width=12)
boton3.grid(row=3,column=1)
boton4 = Button(ventana, text="Menor o =", width=12)
boton4.grid(row=3,column=3)
boton5 = Button(ventana, text="Entre", width=12)
boton5.grid(row=3,column=5)

# titulo
ventana.title("basic statistics")
ventana.mainloop()