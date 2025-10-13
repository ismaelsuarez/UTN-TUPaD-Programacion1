shows= []
entradas= []

while True:
    
    print("\n1.Ingresar shows \n2.Ingresar entradas por show \n3.Mostrar shows/entradas \n4.Consultar entradas de un show",
      "\n5.Listar shows agotados \n6.Agregar show: \n7.Ver agotados \n8.Actualizar entradas (vender/devolución)",
      "\n9.Ver todos los shows \n10.Salir")
    
    opcion=input("Repusta: ").strip()
    if not opcion.isdigit() or opcion=="":
        print("Ingrese una opcion valida")
        continue
    opcion=int(opcion)
    if opcion <= 0 or opcion >=10:
        print("Ingrese un valor del 1 al 10")
    
    match opcion:
        case 1:
            bandera=True
            while bandera:
                cantidad=input("Cuanto show va ingresar: ").strip()
                if not cantidad.isdigit() or cantidad=="":
                    print("Ingreso un valor no permitido, intente de nuevo")
                    continue
                else:
                    cantidad=int(cantidad)
                    for contador in range(cantidad):
                        nuevo=input("Show: ").strip().capitalize()
                        shows.append(nuevo)
                        entradas.append(0)
                        bandera=False 
            bandera=False                       
                
        case 2:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("---------Ingresar entrada por show-----------")                
                for contador in range(len(shows)):
                    bandera=True
                    while bandera:                                  
                        cantidad=input(f"{shows[contador]} Cantidad: ").strip()
                        if not cantidad.isdigit() or cantidad=="":
                            print("Intente de nuevo")
                        else:
                            cantidad=int(cantidad)
                            entradas[contador]=cantidad
                            bandera=False
                    bandera=False
                print("---------------------------------------------")
        case 3:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("--------Lists de shows y sus entradas-----------")
                for contador in range(len(shows)):
                    print(f"{shows[contador]} tiene {entradas[contador]} entradas")
                print("------------------------------------------------")
        case 4:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("---------Consultar entrada por show--------------")
                bandera=True
                while bandera:
                     buscar=input("Show: ").strip().capitalize()
                     if buscar=="":
                         print("Ingreso un nombre no valido")
                         continue
                     else:
                         if buscar in shows:
                             print(f"{buscar} tiene {entradas[shows.index(buscar)]}")
                             bandera=False
                print("-------------------------------------------------")
        case 5:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("----------Shows con entradas agotadas-------------")
                bandera=0
                for contador in range(len(shows)):
                    if entradas[contador]==0:
                        print(f"{shows[contador]} tine {entradas[contador]} entradas")
                        bandera+=1
                if bandera ==0:
                    print("Todos los shows tienen entradas")
                print("--------------------------------------------------")
                
        case 6:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("----------Inrese de show mas su entradas-------------")
                nuevo=input("Show: ").strip().capitalize()
                shows.append(nuevo)
                bandera=True
                while bandera:
                    cantidad=input(f"{shows[contador]} Cantidad: ").strip()
                    if not cantidad.isdigit() or cantidad=="":
                        print("Intente de nuevo")
                    else:
                        cantidad=int(cantidad)
                        entradas.append(cantidad)
                        bandera=False
                bandera=False
                print("-----------------------------------------------------")

        case 7:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("----------Shows con entradas agotadas-------------")
                bandera=0
                for contador in range(len(shows)):
                    if entradas[contador]==0:
                        print(f"{shows[contador]} tine {entradas[contador]} entradas")
                        bandera+=1
                if bandera ==0:
                    print("Todos los shows tienen entradas")
                print("--------------------------------------------------")
        case 8:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                pass
        case 9:
            if not shows:
                print("--------------------------")
                print("-🛑 No hay lista todavia-")
                print("--------------------------")
            else:
                print("----Vender / Devoluciones------")
                buscar=input("Show: ").strip().capitalize()
                if buscar in shows:
                    print("\n")
                
                print("-------------------------------")
        case 10:
            print("Cierre del programa")
            break
        case _:
            print("Ingreso una opcion no valida")

            
                
                