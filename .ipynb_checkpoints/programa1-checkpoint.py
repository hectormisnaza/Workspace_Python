import modulo1
coche1 = modulo1.Coche("Suzuki","gris","gasolina","800")
print (coche1.mostrar_caracteristicas())

media = modulo1.media(3,8,7)
print ("nuestra nota media es {}".format(media))


import moduloficheros

nombre_fichero = 'fichero1.txt'
fichero = moduloficheros.Fichero(nombre_fichero)

texto = '\nEsta es la primera fila del fichero.\nEsta es la segunda fila.'
fichero.grabar_fichero(texto)

texto = '\nEste es un texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)