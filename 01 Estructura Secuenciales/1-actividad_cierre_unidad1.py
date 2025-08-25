#Ejecio numero: 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Ejercicio numero 1") 
print("Hola Mundo")
print("-------------")

#Ejercicio numero: 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
print("Ejercicio numero 2") 
nombre=input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
print("-------------")

#Ejercicio numero: 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
print("Ejercicio numero 3")
print("Ingrese nombre, apellido, edad y de donde es")
nombre=input("Nombre: ")
apellido=input("Apellido: ")
edad=input("edad: ")
residencia=input("De donde es?: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")
print("-------------")

#Ejercicio numero: 4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
print("Ejercicio numero 4")
print("Vamos a descubrir el area y perimetro de un circulo segun su radio")
radio=int(input("Ingrese el radio de un circulo: "))
area=radio*radio
perimetro=2*3.14159*radio
print(f"El area: {area} y su perimeto {perimetro} es el resultado de su radio {radio}")
print("-------------")

#Ejercicio numero 5:
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
print("Ejercicio numero 5")
segundos=int(input("Ingrese la cantidad de segundo, para pasar a hora: "))
horas=segundos/3600
print(f"Los segundos ingresado {segundos} equivalen en horas: {horas}")
print("-------------")

#Ejercicio numero 6:
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
print("Ejercicio numero 6")
numero=int(input("Ingrese un numero para armar su tabla de multiplicar: "))
print(f"{numero} x 1: {numero*1}")
print(f"{numero} x 2: {numero*2}")
print(f"{numero} x 3: {numero*3}")
print(f"{numero} x 4: {numero*4}")
print(f"{numero} x 5: {numero*5}")
print(f"{numero} x 6: {numero*6}")
print(f"{numero} x 7: {numero*7}")
print(f"{numero} x 8: {numero*8}")
print(f"{numero} x 9: {numero*9}")
print("-------------")

#Ejercicio numero: 7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Ejercicio numero 7")
print("Ingrese 2 numeros enteros distintos de 0 para realizar operaciones")
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
print(f"La suma entre  {numero1} y {numero2} es: {numero1+numero2}")
print(f"La division entre  {numero1} y {numero2} es: {numero1/numero2}")
print(f"La multiplicacion entre  {numero1} y {numero2} es: {numero1*numero2}")
print(f"La resta entre  {numero1} y {numero2} es: {numero1-numero2}")
print("-------------")

#Ejercicio numero 8:
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
print("Ejercicio numero 8")
print("Ingrese su altura y peso, para calcular el IMC")
altura=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))
print(f"Su IMC= {peso/altura}")
print("-------------")

#Ejercicio numero 9:
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
print("Ejercicio numero 9")
celsius=float(input("Ingrese los celsius para pasar a fahrenheit: "))
fahrenheit=9/5*celsius+32
print(f"Los celsius {celsius} equivalen en {fahrenheit} fahrenheit")
print("-------------")

#Ejercicio numero 10:
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
print("Ejercicio numero 10")
print("Ingrese 3 numeros para sacar su promedio")
num1=int(input("Primero: "))
num2=int(input("Segundo: "))
num3=int(input("Tercero: "))
print(f"El promedio de {num1} + {num2} + {num3} / 3 es: ",num1+num2+num3/3)
print("-------------")
    