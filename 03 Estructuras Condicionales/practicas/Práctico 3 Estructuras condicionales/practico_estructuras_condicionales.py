#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("-------------------Ejercicio 1-------------------")
numero = int(input("Ingrese su edad: "))
if numero > 18:
    print("Es mayor de edad")
print("--------------------------------------------------")
print("")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 
print("-------------------Ejercicio 2-------------------")
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print("--------------------------------------------------")
print("")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.
print("-------------------Ejercicio 3-------------------")
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print("--------------------------------------------------")
print("")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.
print("-------------------Ejercicio 4-------------------")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
print("--------------------------------------------------")
print("")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.
print("-------------------Ejercicio 5-------------------")
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("--------------------------------------------------")
print("")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
#siguiente: 
#from statistics import mode, median, mean 
#mi_lista = [1,2,5,5,3] 
#mean(mi_lista) 
#En la documentación oficial se puede encontrar más información sobre este paquete: 
#https://docs.python.org/es/3.8/library/statistics.html.  
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
#● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma: 

import random 
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
print("-------------------Ejercicio 6-------------------")
print("Lista de numeros aleatorios: ")
print(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")
if media > mediana and media > moda:
    print("Sesgo positivo")
elif media < mediana and media < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")
print("--------------------------------------------------")
print("")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 
print("-------------------Ejercicio 7-------------------")
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase +"!")
else:
    print(frase)
print("--------------------------------------------------")
print("")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
print("-------------------Ejercicio 8-------------------")
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: "))
if opcion ==1:
    print(f"Su nombre en mayusculas es: {nombre.upper()}")
elif opcion ==2:
    print(f"Su nombre en minusculas es: {nombre.lower()}")
elif opcion ==3:
    print(f"Su nombre con la primera letra en mayuscula es: {nombre.title()}")
else:
    print("Opcion incorrecta")
print("--------------------------------------------------")
print("")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
print("-------------------Ejercicio 9-------------------")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")  
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
print("--------------------------------------------------")
print("")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
#Estación en el hemisferio norte:Invierno
#Estación en el hemisferio sur:Verano
#Desde el 21 de marzo hasta el 20 de junio (incluidos)
#Estación en el hemisferio norte: Primavera
#Estación en el hemisferio sur: Otoño
#Desde el 21 de junio hasta el 20 de septiembre (incluidos)
#Estación en el hemisferio norte: Verano
#Estación en el hemisferio sur: Invierno
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
#Estación en el hemisferio norte: Otoño
#Estación en el hemisferio sur: Primavera
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.
print("-------------------Ejercicio 10-------------------")
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia= int(input("Ingrese el dia (1-31): "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print("Verano")
    else:
        print("Otoño")
if hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print("Invierno")
    else:
        print("Primavera")
print("--------------------------------------------------")
print("")   
