#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("-----Ejercio 1-----")
for num in range(101):
    print(num)
print("--------------------")
print("")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
print("-----Ejercio 2-----")
num=int(input("Ingrese un numero entero: "))    
contador=0
while num!=0:
    num=num//10
    contador+=1 
print("La cantidad de digitos es: ",contador)
print("--------------------")
print("")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

print("-----Ejercio 3-----")   
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))  
suma=0
for num in range(num1+1,num2):
    suma+=num     
    print(suma)          
print("La suma de los numeros entre ",num1," y ",num2," es: ",suma+num1+num2)
print("--------------------")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("-----Ejercio 4-----")
suma=0
print("Ingrese los numero que quiere sumar, cuando ponga 0 le va a mostrar el total")
while suma >= 0:
    num=int(input("Numero: "))
    if num == 0:
        break
    suma+=num
print(f"La suma de todos los enteros ingresado es: {suma}")

print("--------------------")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("-----Ejercio 5-----")
import random
aleatorio=random.randint(0, 9)
suma=0
asierto=0
print("Ingrese un numero, para adivinar el numero oculto")

while asierto !=aleatorio:
    asierto=int(input("Numero: "))
    if asierto != aleatorio:
        suma +=1
print(f"Pudo adivinar en {suma} intentos")
print("--------------------")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

print("-----Ejercio 6-----")
print("Numero pares entre el 0 y 100 de forma decreciente")
for numero in range(100, -1, -2):
  print(numero)
print("--------------------")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("-----Ejercio 7-----")

print("Ingrese el numero hasta cual quiere sumar desde el 0 hasta x")
num1=int(input("Numero: "))
suma=0
for num in range(num1+1):
    suma+=num     
    print(suma)          
print("La suma de los numeros entre 0 y ",num1," es: ",suma)

print("--------------------")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("-----Ejercio 8-----")

print("Ingrese 100 numeros enteros, y se le informara cuantos positivos y negativos hay, pares, impares tambien")
num=100
positivo=0
negativo=0
par=0
impar=0
for cont in range(1, num+1):
    num1=int(input(f"{cont} Numero: "))
    if num1 >=0:
        positivo +=1
    elif num1 <0:
        negativo+=1
    if num1 % 2 == 0:
        par +=1
    else:
        impar+=1
print(f"Cantidad de numeros positivos: {positivo}, negativos {negativo} \n cantidad de numeros pares {par} e impares {impar}")

print("--------------------")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

print("-----Ejercio 9-----")

num=100
suma=0
print("Ingrese 100 numeros enteros para evaluar su media")
for cont in range(1,num+1):
    num1=int(input(f"{cont} - Numero: "))
    suma +=num1

print(f"La media de {num} numeros ingresados es: {suma/num}")
print("--------------------")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("-----Ejercio 9-----")

numero_original = int(input("Ingresa un número: "))
numero_invertido = 0
numero_temporal = numero_original
while numero_temporal > 0:
        ultimo_digito = numero_temporal % 10
        numero_invertido = (numero_invertido * 10) + ultimo_digito
        numero_temporal = numero_temporal // 10
print(f"El número original es: {numero_original}")
print(f"El número invertido es: {numero_invertido}")
print("--------------------")
