
# Mensaje de Bienvenida
print ("¡Bienvenido al Buscador!\nPor favor, ingrese el Texto.")

# Proceso
texto = str (input())
texto_t=texto.capitalize()

print ("Por favor, ingrese una Palabra a buscar.")
palabra = str (input())

cuenta= texto_t.count (palabra)

#Resultado
if cuenta > 0:
    print ("Se han encontrado: "+ str(cuenta) + " coincidencia/s.")
if cuenta == 0:
    print ("No se han encontrado coincidencias.")
