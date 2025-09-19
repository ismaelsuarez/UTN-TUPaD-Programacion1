#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
print("---------Ejercicio 1---------")

numeros=[] #Inicializo la lista vacia
for cont in range(1,101): #For para llenar la lista
    if cont % 4 ==0: #Condicion para asegurarme que numeros son multiplos de 4
        numeros.append(cont) #Se cargan los numeros que cumplen la condicion
print(numeros) #Se muestra la lista creada

print("-----------------------------")

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
#indexing con números negativos! 

print("---------Ejercicio 2---------")
import random #Importa la funcion random
elementos=[] #Inicializo la lista vacia
for cont in range(5):#For para llenar la lista
    numero=random.randint(0,10) #Genero numero aleatorio de 0 hasta 10
    elementos.append(numero)#Lleno la lista con numeros aleatorios
print(f"Lista: {elementos}") #Imprimo lista
print(f"El penultimo elemento: {elementos[3]}") #Imprimo el resultado

print("-----------------------------")
#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: lista_vacia = []
print("---------Ejercicio 3---------")
print("Ingrese 3 palabras al azar: ") #Pido que ingrese numero al azar
lista=[] #Inicializo la lista vacia
for cont in range(3): #For para llenar la lista
    palabra=input("Palabra: ") #Pido la palabra a ingresar en la lista
    lista.append(palabra) #Ingreso la palabra informada por el usuario a la lista
print(lista) #Imprimo la lista
print("-----------------------------")

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
#animales = ["perro", "gato", "conejo", "pez"]
print("---------Ejercicio 4---------")
animales = ["perro", "gato", "conejo", "pez"] #Lista inicializada con elementos

print(F"Lista original {animales}") #Imprimo la lista inicializada
for cont in range(len(animales)): #For para llenar la lista
    if cont==1: #condicional para ingresar a un lugar especifico 
        animales[cont]="loro" #Edito el elemento con un nuevo elemento
    elif cont==(len(animales)-1): #condicional para ingresar a un lugar especifico 
        animales[cont]="oso" #Edito el elemento con un nuevo elemento
print(f"Lista modificada: {animales}") #Imprimo la nueva lista modificada

print("-----------------------------")

print("---------Ejercicio 5---------")
#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros=[8,15,3,22,7] #Lista inicializada con elementos
numeros.remove(max(numeros)) #Itera la lista en busqueda del numero mayor y lo borra
print(numeros) #Imprime la lista modificada
#Itera la lista de nuemros con la funcion max en  busca del mayor numero y lo borra
print("Itera la lista de nuemros con la funcion max en  busca del mayor numero y lo borra")
print("-----------------------------")

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros. 
print("---------Ejercicio 6---------")
lista=[] #Inicializo la lista vacia
for cont in range(10,31,5): #For para llenar la lista
    lista.append(cont) #Lleno la listsa con los numeros que se generan
print(f"Lista: {lista}") #Muestro la lista completa
print(f"Elemento en primer lugar: {lista[0]}") #Muestro un elemento especifico
print(f"Elemento en segundo lugar: {lista[1]}") #Muestro un elemento especifico

print("-----------------------------")

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
print("---------Ejercicio 7--------")

autos = ["sedan", "polo", "suran", "gol"] #Lista inicializada con elementos
print(f"Lista sin modificar: {autos}") #Imprimo la lista sin modificar
for cont in range(1,3): #For para llenar la lista
    resp=input("Cambio: ") #Pido el nuevo elemento para actualizar
    autos[cont]=resp #Ingreso el nuevo elemento
print(f"Lista sin modificada: {autos}") #Imprimo la nueva lista

print("-----------------------------")

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 

print("---------Ejercicio 8--------")
dobles=[] #Inicializo la lista vacia
for cont in range(5,20,5): #For para llenar la lista
    dobles.append(cont*2) #Actualizo la lista, con su dobre segun el elemento
print(dobles) #Imprimo la lista modificada
print("-----------------------------")

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla 
print("---------Ejercicio 9--------")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]  #Lista inicializada con elementos
print(f"Listas sin modificar: {compras}") #Imprimo la lista original
for cont in range(len(compras)): #For para llenar la lista
    if "pan" in compras[cont]: #condicional para ingresar a un lugar especifico 
        compras[cont].remove("pan") #Se borra el elemento
    if "fideos" in compras[cont]: #condicional para ingresar a un lugar especifico 
        mod=compras[cont].index("fideos") #Se modifica el elemento en una variable
        compras[cont][mod]="tallarines" # Se usa la variable para modificar el elemento
    if "agua" in compras[cont]: #condicional para ingresar a un lugar especifico 
        mod=compras[cont].index("agua") #Se modifica el elemento en una variable
        compras[cont][mod]="juego" # Se usa la variable para modificar el elemento
              
print(f"Lista modificada: {compras}")

print("-----------------------------")

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla.
print("---------Ejercicio 10--------")
lista_anidada=[[15],[True],[0,1,2],[False]] #Se crea unna lista anidada
print(lista_anidada) # Se imprime la lista anidada
print("-----------------------------")
