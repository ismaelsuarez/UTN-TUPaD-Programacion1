clases = []
cupos = []

while True:
    print("-----------Manu-----------")  # Armo el Manu
    print("\n1.Ingresar lista de clases \n2.Ingresar cupos por clase \n3.Mostrar clases con cupos \n4.Consultar cupo de una clase",
          "\n5.Listar clases sin cupo \n6.Agregar clase \n7.Ver sin cupo \n8.Actualizar cupos (inscribir/baja)",
          "\n9.Ver todas clases \n10.Salir")

    # Valido si esta bien lo que ingreso el usuario
    opcion = input("Opcion: ").strip()
    if not opcion.isdigit() or opcion == "":  # Condicion por si esta mal, lo informo
        print("--------------Error--------------")
        print("🛑 Ingrese un numero del 1 al 10")
        print("--------------Error--------------")
    opcion = int(opcion)  # Parseo el string a int

    match opcion:  # Creo las opciones segun la opcion seleccionada
        case 1:  # Creo la lista de clases
            bandera = True  # Utilizo la badera, para salir del while
            while bandera:  # Utilizo el while, para darle la opcion a poder seguir                
                cantidad = input("Cuanta clases va a ingresar: ").strip() # Consulto la cantidad a ingresar
                if not cantidad.isdigit() or cantidad == "":  # Verifico que ingreso un numero
                    print("Ingrese la cantidad en numero por favor del 1 al 10")
                cantidad = int(cantidad)
                if cantidad <= 0 or cantidad > 10:  # Verifico que no ingreso un numero negativo o mayo a 10
                    print("Ingrese la cantidad en numero por favor del 1 al 10")
                else:
                    # Creo la lista, segun la cantidad de nombre va a ingresar
                    for contador in range(cantidad):
                        # Pido el nombre de la clase
                        clase = input("Clase: ").strip().capitalize()
                        # Ingreso el Nombre de la clase a la lista clases
                        clases.append(clase)
                        # Inicializo en 0 el cupo de la lista Cupos, que le pertenece al nombre que ingreso
                        cupos.append(0)
                    bandera = False 
            bandera = False  # Salgo del while
        case 2:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("-----Ingreso de Cupos-------")
                bandera = True  # Utilizo la badera, para salir del while
                while bandera:  # Utilizo el while, para darle la opcion a poder seguir
                    # Itero la lista, para cargar los cupos
                    for contador in range(len(clases)):
                        cupo = input(f"Clase: {clases[contador]} Cupo: ").strip()
                        if not cupo.isdigit():
                            print("Ingrese la cantidad en numeros")
                        else:
                            cupo = int(cupo)
                            cupos[contador] = cupo
                    bandera = False
                print("----------------------------")
        case 3:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("-------Lista de Clase-----------")
                for contador in range(len(clases)):
                    print(f"{clases[contador]} tiene {cupos[contador]} cupos")
                print("--------------------------------")
        case 4:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("---------Consulta de cupos-----------")
                bandera = True  # Utilizo la badera, para salir del while
                while bandera:
                    clase = (input("Clase: ")).strip().capitalize()
                    if clase.isdigit() or clase == "":
                        print("Ingrese un Nombre de clase")
                    if clase in clases:
                        print(
                            f"Clase: {clase} tiene {cupos[clases.index(clase)]} cupos")
                        bandera = False
                    else:
                        print(
                            "No tenemos esa clase en nuestra base de datos \n*Intente de nuevo*")
                        continue
                print("-------------------------------------")
        case 5:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("------------Clases sin Cupos-------------")
                bandera=0
                for contador in range(len(clases)):
                    if cupos[contador] == 0:
                        print(f"{clases[contador]} tiene {cupos[contador]} clases")
                        bandera+=1
                if bandera == 0:
                    print("Todas las clases tienen cupos")
                print("-----------------------------------------")
        case 6:
            print("-------Ingrese de clase + cupos-----------")
            bandera = True  # Utilizo la badera, para salir del while
            clase = input("Clase: ").strip().capitalize()
            clases.append(clase)
            while bandera:
                cupo = input("Cupos: ")
                if not cupo.isdigit() or cupo == "":
                    print("Ingrese un numero valido, intente de nuevo")
                    continue
                cupo = int(cupo)
                cupos.append(cupo)
                bandera = False
            print("------------------------------------------")

        case 7:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("------------Clases sin Cupos-------------")
                for contador in range(len(clases)):
                    if cupos[contador] == 0:
                        print(
                            f"{clases[contador]} tiene {cupos[contador]} clases")
                if cupos[contador] > 0:
                    print("Todas las clases tienen cupos")
                print("-----------------------------------------")

        case 8:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("----Inscribir o dar de baja cupos----------")
                buscar = input("Clase: ").strip().capitalize()
                if buscar in clases:
                    respuesta = input("\n1-Inscribir \n2-Baja \nRepuesta: ")
                    respuesta = int(respuesta)
                    match respuesta:
                        case 1:
                            bandera = True  # Utilizo la badera, para salir del while
                            while bandera:
                                cantidad = input("Cantida: ")
                                if not cantidad.isdigit() or cantidad == "":
                                    print(
                                        "Ingrese un valor valido, intente de nuevo")
                                    continue
                                else:
                                    cantidad = int(cantidad)
                                    cupos[clases.index(buscar)] += cantidad
                                    bandera = False
                        case 2:
                            bandera = True  # Utilizo la badera, para salir del while
                            while bandera:
                                cantidad = input("Cantida: ")
                                if not cantidad.isdigit() or cantidad == "":
                                    print(
                                        "Ingrese un valor valido, intente de nuevo")
                                    continue
                                else:
                                    cantidad = int(cantidad)
                                    if cantidad > cupos[clases.index(buscar)]:
                                        cupos[clases.index(buscar)] = 0
                                        bandera = False
                                    else:
                                        cantidad = int(cantidad)
                                        cupos[clases.index(buscar)] -= cantidad
                                        bandera = False
                else:
                    print("No tenemos esa clase en el registro")
                print("-------------------------------------------")
        case 9:
            if not clases:  # Verifico primero que exista una lista, si no exite lo informo
                print("-------------------------")
                print("🛑 No hay clases cargadas")
                print("-------------------------")
            else:
                print("-------Lista de Clase-----------")
                for contador in range(len(clases)):
                    print(f"{clases[contador]} tiene {cupos[contador]} cupos")
                print("--------------------------------")
        case 10:
            print("Cierre del programa")
            break
        case _:
            pass
