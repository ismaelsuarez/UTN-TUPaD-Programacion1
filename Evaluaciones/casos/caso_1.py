#Caso 1 – Biblioteca escolar – Préstamos de libros
#Enunciado / Descripción
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.
#Ejemplo:
#•	títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
#•	ejemplares[] = [5, 3, 7]
#En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias, y "Matar un Ruiseñor" tiene 7 copias.
#Opciones del Menú:
#1.	Ingresar lista de títulos:
#o	Permite al usuario introducir los títulos de los libros en la biblioteca.
#o	Ejemplo: El usuario introduce "1984", "Rebelión en la Granja".
#2.	Ingresar lista de ejemplares disponibles (por título):
#o	Permite al usuario introducir el número de copias disponibles para cada título de libro.
#o	Ejemplo: Si el título es "1984", el usuario podría introducir "4" (lo que significa que hay 4 copias).
#3.	Mostrar catálogo con stock:
#o	Muestra una lista de todos los títulos y el número de copias disponibles para cada uno.
#o	Ejemplo de salida:
#	"El Señor de los Anillos: 5 copias"
#	"Orgullo y Prejuicio: 3 copias"
#	"Matar un Ruiseñor: 7 copias"
#4.	Consultar disponibilidad de un título específico:
#o	Permite al usuario introducir un título y ver cuántas copias están disponibles.
#o	Ejemplo: El usuario introduce "Orgullo y Prejuicio", y el programa muestra "3 copias disponibles".
#5.	Listar agotados (0 ejemplares):
#o	Muestra una lista de todos los títulos que tienen 0 copias disponibles.
#6.	Agregar título:
#o	Permite al usuario añadir un nuevo título al catálogo y especificar el número inicial de copias.
#7.	Ver títulos agotados:
#o	Muestra una lista de los títulos con cero copias disponibles.
#8.	Actualizar ejemplares (préstamo/devolución):
#o	Permite al usuario actualizar el número de copias cuando un libro es prestado (préstamo) o devuelto (devolución).
#o	Ejemplo: Si alguien toma prestada una copia de "El Señor de los Anillos", el usuario puede actualizar el conteo de 5 a 4.
#9.	Ver catálogo:
#o	Muestra el catálogo entero de los títulos de libros.
#10.	Salir:
#o	Sale del programa.
 
print("Sistema de Gestión de Biblioteca Escolar")
titulos = []
ejemplares = []
print("-------------------------")

resp=1
while resp >= 1 and resp <= 10:
    print("-------------------------")
    print("Menú de opciones:")
    resp=int(input("Ingrese la opcion del menu: \n1. Ingresar lista de títulos \n2. Ingresar lista de ejemplares disponibles (por título) \n3. Mostrar catálogo con stock \n4. Consultar disponibilidad de un título específico \n5. Listar agotados (0 ejemplares) \n6. Agregar título \n7. Ver títulos agotados \n8. Actualizar ejemplares (préstamo/devolución) \n9. Ver catálogo \n10. Salir \n"))
    if resp<=0:
        print("Opción no válida. Por favor, elija una opción del 1 al 10.")
    if resp ==1:
        ingresos=int(input("Cuantos titulos quiere ingresar: "))
        for cont in range(ingresos):
            titulo=input("Ingrese el titulo del libro: ")
            titulos.append(titulo)
    if resp ==2:
         for cont in range(len(titulos)):
            ejemplares.append(int(input(f"Ingrese la cantidad de ejemplares disponibles para '{titulos[cont]}': ")))
    if resp == 3:
        for cont in range(len(titulos)):  
            if ejemplares[cont]>0:      
             print(f"titulos: {titulos[cont]} tiene ejemplares: {ejemplares[cont]}")    
    if resp == 4: 
        consulta=input("Ingrese el titulo a consultar: ")
        for cont in range(len(titulos)):
            if consulta == titulos[cont]:
                print(f"El titulo {consulta} tiene {ejemplares[cont]} ejemplares")
                break
    if resp ==5:
        print("Titulos agotados: ")
        for cont in range(len(titulos)):
            if ejemplares[cont] == 0:
                print(f"El titulo: {titulos[cont]} no tiene ejemplares")
                break
    if resp ==6:
        for con in range(1):
            for cont in range(1):                
             nuevo_titulo=input("Ingrese el nuevo titulo: ")
             nuevo_ejemplar=int(input("Ingres la cantidad de ejemplares: "))
            titulos.append(nuevo_titulo)
            ejemplares.append(nuevo_ejemplar)
            print(f"Se agrego el titulo: {nuevo_titulo} con {nuevo_ejemplar} ejemplares")
            break
    
    if resp ==7:
        print("Titulos agotados:")
        for cont in range(len(titulos)):
            if ejemplares[cont]==0:
                print(f"El titulo: {titulos[cont]} no tiene ejemplares")
                break
    if resp ==8:
        actualizar=input("Ingrese el titulo a actualizar: ")
        for cont in range(len(titulos)):
            if actualizar == titulos[cont]:
                print(f"El titulo {actualizar} tiene {ejemplares[cont]} ejemplares")
                accion=input("Ingrese 'P' para préstamo o 'D' para devolución: ").upper()
                if accion == 'P':
                    if ejemplares[cont] > 0:
                        ejemplares[cont] -= 1
                        print(f"Préstamo realizado. Ahora '{actualizar}' tiene {ejemplares[cont]} ejemplares.")
                    else:
                        print(f"No hay ejemplares disponibles para '{actualizar}'.")
                elif accion == 'D':
                    ejemplares[cont] += 1
                    print(f"Devolución realizada. Ahora '{actualizar}' tiene {ejemplares[cont]} ejemplares.")
                else:
                    print("Acción no válida. Por favor, ingrese 'P' o 'D'.")
                break        
    if resp ==9:
        print("Catalogo completo: ")
        for cont in range(len(titulos)):
            print(f"El titulo: {titulos[cont]} tiene {ejemplares[cont]} ejemplares")
    if resp ==10:
        print("Saliendo del programa...")
        break
    