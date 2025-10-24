precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

print("**********Ejercicio 1**********")
#Añadir las siguientes frutas con sus respectivos precios:
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

print(precios_frutas)
print("******************************************")

print("**********Ejercicio 2**********")
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melon = 2800

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melon"]=2800

print(precios_frutas)
print("******************************************")

print("**********Ejercicio 3**********")
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)
print("******************************************")

print("**********Ejercicio 4**********")

# Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 
#Ejemplo: contactos = {"Juan": "123456", "Anana": "987654"}
#consultar: "Juan" = Muestra "123456"

contactos={}
for i in range(5):
    nombre=input("Ingrese el nombre del contacto: ").capitalize().strip()
    numero=input("Ingrese el numero telefonico: ")
    contactos[nombre]=numero
print("Contactos cargados.")
consultar=input("Ingrese el nombre a consultar: ")
if consultar in contactos:
    print(f"El numero de {consultar} es {contactos[consultar]}")
else:
    print(f"No existe un contacto con el nombre {consultar}")
print("******************************************")
print("**********Ejercicio 5**********")

# Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.
#Ejemplo: palabras_unicas:{"hola", "mundo"}
# Recuento: {"hola": 2, "mundo": 1}
frase=input("Ingrese una frase: ").strip().capitalize()
palabras=frase.split()
palabras_unicas=set(palabras)
print("Palabras únicas:", palabras_unicas)
recuento={}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra]+=1
    else:
        recuento[palabra]=1 
print("Recuento de palabras:", recuento)
print("******************************************")

print("**********Ejercicio 6**********")
#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 
#Ejemplo: alumnos={"Sofia": (10,9,8), "Luis": (6,7,7)} 
alumnos={}
for i in range(3):
    nombre=input("Ingrese el nombre del alumno: ").capitalize().strip()
    notas=[]
    for j in range(3):
        nota=float(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)
    alumnos[nombre]=tuple(notas)
print(alumnos)

print("******************************************")
print("**********Ejercicio 7**********")
#) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial_1={101, 102, 103, 104, 105}
parcial_2={104, 105, 106, 107, 108}
aprobados_ambos=parcial_1.intersection(parcial_2)
solo_uno=parcial_1.symmetric_difference(parcial_2)
total_aprobados=parcial_1.union(parcial_2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)
print("Lista total de estudiantes que aprobaron al menos un parcial:", total_aprobados)
print("******************************************")
print("**********Ejercicio 8**********")

# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.

producto={}
while True:
    print("****Menu****\n1. Consultar stock\n2. Agregar unidades al stock\n3. Agregar nuevo producto\n4. Salir")
    opcion=input("Seleccione una opción (1-4): ")
    match opcion:
        case "1":
            if not producto:
                print("No hay productos en el inventario.")
            else:
                consultar=input("Ingrese el nombre: ").strip().capitalize()
                if consultar in producto:
                    print(f"El stock de {consultar} es: {producto[consultar]}")
                else:
                    print(f"El producto {consultar} no existe en el inventario.")
        case "2":
                agregar=input("Ingrese el nombre del producto a agregar unidades: ").strip().capitalize()
                if agregar in producto:
                    try:
                        unidades=int(input("Ingrese la cantidad de unidades a agregar: "))
                        if unidades < 0:
                            print("No se pueden agregar unidades negativas.")
                        else:
                            producto[agregar] += unidades
                            print(f"Nuevo stock de {agregar}: {producto[agregar]}")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                else:
                    print(f"El producto {agregar} no existe en el inventario.")
                
        case "3": 
            nuevo_producto=input("Ingrese el nombre del nuevo producto: ").strip().capitalize()
            if nuevo_producto in producto:
                print(f"El producto {nuevo_producto} ya existe en el inventario.")
            else:
                try:
                    stock_inicial=int(input("Ingrese el stock inicial: "))
                    if stock_inicial < 0:
                        print("El stock no puede ser negativo.")
                    else:
                        producto[nuevo_producto]=stock_inicial
                        print(f"Producto {nuevo_producto} agregado con stock {stock_inicial}.")
                except ValueError:
                    print("Por favor, ingrese un número válido para el stock.")
        case "4":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")
print("******************************************")
print("**********Ejercicio 9**********")
#  Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Ejemplo: agenda = {"lunes", "10:00):"Reunion", ("lunes","15:00):"Clases de ingles)} 
agenda={}
while True: 
    print("****Menu Agenda****\n1. Agregar evento\n2. Consultar evento\n3. Salir")
    opcion=input("Seleccione una opción (1-3): ")
    match opcion:
        case "1":
            dia=input("Ingrese el día del evento (ejemplo: lunes): ").strip().lower()
            hora=input("Ingrese la hora del evento (formato 24h, ejem: 14:30): ").strip()
            evento=input("Ingrese la descripción del evento: ").strip()
            agenda[(dia, hora)]=evento
            print(f"Evento '{evento}' agregado para el {dia} a las {hora}.")
        case "2":
            dia_consulta=input("Ingrese el día a consultar (ejemplo: lunes): ").strip().lower()
            hora_consulta=input("Ingrese la hora a consultar (formato 24h, ejem: 14:30): ").strip()
            clave=(dia_consulta, hora_consulta)
            if clave in agenda:
                print(f"Evento para el {dia_consulta} a las {hora_consulta}: {agenda[clave]}")
            else:
                print(f"No hay eventos programados para el {dia_consulta} a las {hora_consulta}.")
        case "3":
            print("Saliendo de la agenda.")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")
print("******************************************")
print("**********Ejercicio 10**********")
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 
# Ejemplo: original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
paises_capitales={"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Uruguay": "Montevideo"}
capitales_paises={}
for pais, capital in paises_capitales.items():
    capitales_paises[capital]=pais  
print("Diccionario invertido:", capitales_paises)
print("******************************************")

