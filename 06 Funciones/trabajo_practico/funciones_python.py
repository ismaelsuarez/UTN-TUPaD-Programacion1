#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.
print("----------Ejercicio 1---------------")
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
print("------------------------------------")

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

print("----------Ejercicio 2---------------")
def saludar_usuario(nombre):
    return print(f"Hola {nombre}")

nombre=input("Ingrese su nombre: ").strip().capitalize()
if nombre=="" or nombre.isspace():
    print("No ingresó ningún nombre.")
else:
    saludar_usuario(nombre)
print("------------------------------------")

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

print("----------Ejercicio 3---------------")
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
informacion_personal(input("Ingrese su nombre: ").strip().capitalize(),
                     input("Ingrese su apellido: ").strip().capitalize(),
                     input("Ingrese su edad: ").strip(),
                     input("Ingrese su residencia: ").strip().capitalize())
print("------------------------------------")

#4. Crear dos funciones: calcular_area_circulo(radio)
# que reciba el radio como parámetro y devuelva el área 
# del círculo. calcular_perimetro_circulo(radio) que reciba 
# el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

print("----------Ejercicio 4---------------")

import math
def calcular_area_circulo(radio):
    area=math.pi * radio**2
    return area

def calcular_perimetro_circulo(radio):
    perimetro=2 * math.pi * radio
    return perimetro

radio=float(input("Ingrese el radio del circulo: "))
area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")
print("------------------------------------")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar 
# el resultado usando esta función.
print("----------Ejercicio 5---------------")
def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas

segundos=int(input("Ingrese la cantidad de segundos: "))

print(f"La cantidad de {segundos} en horas son: {segundos_a_horas(segundos)}")
print("------------------------------------")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.
print("----------Ejercicio 6---------------")
def tabla_multiplicar(numero):
        for i in range(1,11):
            print(f"{numero} x {i} = {numero*i}")

numero=int(input("Ingrese un numero para mostrar su tabla de multiplicar: " ))
if numero==0 :
    print("La tabla del 0 es siempre 0. y ingreso un valor invalido")
else:
    tabla_multiplicar(numero)
print("------------------------------------")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los 
# resultados de forma clara.

print("----------Ejercicio 7---------------")
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicar=a*b
    dividir=a/b
    operaciones=(suma, resta, multiplicar, dividir)
    return operaciones

a=float(input("Ingrese el primer numero: "))
b=float(input("Ingrese el segundo numero: "))

if b==0 or a==0:
    print("No se puede dividir por 0. Ingreso un valor invalido")
else:
    suma, resta, multiplicar, dividir=operaciones_basicas(a,b)
    print(f"La suma es: {suma} \nLa resta es: {resta} \nLa multiplicacion es: {multiplicar} \nLa division es: {dividir}")
    
print("------------------------------------")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
# función para mostrar el resultado con dos decimales.

print("----------Ejercicio 8---------------")
def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    return imc
print("Calcular indice de masa corporal (IMC)")
peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en metros: "))
imc=calcular_imc(peso, altura)
print(f"Su indice de masa corporal es: {imc}")

print("------------------------------------")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.      

print("----------Ejercicio 9---------------")
def celsius_a_fahrenheit(celsius):
    fahrenheit=(celsius * 9/5) + 32
    return fahrenheit

celsius=float(input("Ingrese la temperatura: ")) 
repuesta=celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {repuesta}")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

print("----------Ejercicio 10--------------")
def calcular_promedio(a ,b ,c):
    promedio=(a+b+c)/3
    return promedio

print("Calcular el promedio de 3 numeros")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))

promedio=calcular_promedio(num1, num2, num3)
print(f"El promedio de los numeros es: {promedio}")
print("------------------------------------")
