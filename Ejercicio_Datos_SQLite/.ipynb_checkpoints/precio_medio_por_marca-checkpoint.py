
def precio_medio_por_marca(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT marca, AVG(precio) FROM coches GROUP BY marca")
    datos = cursor.fetchall()
    return datos


print("\n Precio medio por marca \n")
datos = precio_medio_por_marca(conexion)
for dato in datos:
    marca = dato[0]
    precio = dato[1]
    print(marca,precio)

