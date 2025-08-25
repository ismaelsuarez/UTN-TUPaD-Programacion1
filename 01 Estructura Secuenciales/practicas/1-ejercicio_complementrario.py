
print("-----------")
print("Ejercicio_1")
print(" ")
#Crea una variable "numero1" y asignale un numero entero de tu eleccion
print(" ")
numero1=55

print(" ")
print("-----------")
print("Ejercicio_2")
#No borres la variable número uno y crea una variable llamada "numero2" asignándole
#un número decimal de tu elección.
print(" ")
numero2=7.5

print(" ")
print("-----------")
print("Ejercicio_3")
#Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
print(" ")
suma=numero1 + numero2
print(f"El valor de la suma entre {numero1} y {numero2} es: {suma}")

print(" ")
print("-----------")
print("Ejercicio_4")
#Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
#multiplicación y otra para división. Imprime estas variables.
print(" ")
resta= numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2

print(f'La resta de {numero1} y {numero2} es: {resta}')
print(f'La multiplicacion de {numero1} y {numero2} es: {multiplicacion}')
print(f'La division de {numero1} y {numero2} es: {division}')

print(" ")
print("-----------")
print("Ejercicio_5")
#Crea una variable llamada "nombre" y asígnale tu nombre como valor.
print(" ")
nombre="Ismael"

print(" ")
print("-----------")
print("Ejercicio_6")
#Crea una variable llamada "precio" y asígnale un valor decimal que represente el
#precio de un artículo ficticio.
print(" ")
precio=55.5

print(" ")
print("-----------")
print("Ejercicio_7")
#Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
#100% y el valor 0 al 0%.
print(" ")
descuento=25
print(f"El valor de descuento aplicado es de: {descuento}")

print(" ")
print("-----------")
print("Ejercicio_8")
#Ahora, intenta calcular el precio final aplicando el descuento al precio original y
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
#aplicar la lógica de matemáticas.
print(" ")
precio_final=precio / ( (descuento/100)+1)

print(" ")
print("-----------")
print("Ejercicio_9")
#Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
#elección. Qué sea un string.
print(" ")
cadena="Vamos a programar!!"

print(" ")
print("-----------")
print("Ejercicio_10")
#Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
#a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
#Python.
print(" ")
longitud=len(cadena)
print(f"La longitud de {cadena} es: {longitud}")


print(" ")
print("-----------")
print("Ejercicio_11")
# Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
#conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
#mismo.
print(" ")
precio=float(55.5)


print(" ")
print("-----------")
print("Ejercicio_12")
#Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.
print(" ")
nombre="Ismael"
apellido="Suarez"
nombre_completo= nombre +" "+ apellido

print(" ")
print("-----------")
print("Ejercicio_13")
#Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
print(" ")
edad=40
edad_mas_5=edad + 5
edad_menos_10=edad - 10
print(f"Su edad: {edad}, mas 5 son: {edad_mas_5}, menos 10 son: {edad_menos_10}")


print(" ")
print("-----------")
print("Ejercicio_14")
#Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
#centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.
print(" ")
altura= 1.87
resultado= (altura * 4) / 3
print(f"El resultado es: {resultado}")

print(" ")
print("-----------")
print("Ejercicio_15")
# Crea una variable que contenga tu nombre completamente en mayúsculas. Después
#transfórmalo todo en minúsculas con algún método o función de Python.
print(" ")
nombre_mayuscula= "ISMAEL"
nombre_minuscula= nombre_mayuscula.lower()
print(nombre_minuscula)

print(" ")
print("-----------")
print("Ejercicio_16")
#Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#para que se transforme todo en minúsculas excepto la primera letra.
nombre_primera_en_minuscula=nombre_mayuscula[0].upper()
demas_mayusculas=nombre_mayuscula[1:].lower()
frase=nombre_primera_en_minuscula+demas_mayusculas
print(frase)









