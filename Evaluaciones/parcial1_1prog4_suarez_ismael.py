titulos=[]
ejemplares=[]

while True:
    
    print("\n1. Ingresar títulos \n2. Ingresar ejemplares \n3. Mostrar catálogo \n4. Consultar disponibilidad",
          "\n5. Listar agotados \n6. Agregar título \n7. Actualizar ejemplares (préstamo/devolución) \n8. Salir")
    opcion=input("Opcion: ").strip()
    if not opcion.isdigit() or opcion=="":
        print("Ingreso un valor erroneo, intente nuevamente")
        continue
    opcion=int(opcion)
    
    if opcion<=0 or opcion>8:
        print("Debe ingresar un valor del 1 al 8")
        print("Intente nuevamente")
        continue
    
    match opcion:
        case 1:
            print("--------Ingreso de Titulos----------")
            bandera=True
            while bandera:
                cantidad=input("Cuanto titulos va a ingresar: ").strip().capitalize()
                if not cantidad.isdigit() or cantidad=="":
                    print("Ingreso un valor que no corresponde")
                    print("Intene nuevamente")
                    continue
                cantidad=int(cantidad)
                if cantidad<=0:
                    print("Ingrese un valor entero posivo apartir del 1")
                    print("Intente nuevamente")
                    continue
                for contador in range(cantidad):
                    nuevo=input("Titulo: ").strip().capitalize()
                    titulos.append(nuevo)
                    ejemplares.append(0)
                    bandera=False 
            bandera=False          
            print("------------------------------------")
        case 2:
            print("-------Ingresar Ejemplares-----")
            for contador in range(len(titulos)):
                bandera=True
                while bandera:
                    ejemplar=input(f"{titulos[contador]} cantidad de ejemplar: ").strip()
                    if not ejemplar.isdigit() or ejemplar=="":
                        print("Ingreso un valor que no corresponde")
                        print("Intente nuevamente")
                        continue
                    ejemplar=int(ejemplar)
                    ejemplares[contador]=ejemplar
                    bandera=False                
                print("-------------------------------")
        case 3:
            if  not titulos:
                print("-------------------------------")
                print("NO Hay titulos cargador todavia")
                print("-------------------------------")
            else:
                print("----------Catalogo con stock-----------")
                for contador in range(len(titulos)):
                    print(f"* {titulos[contador]} tiene {ejemplares[contador]} de ejemplares")
                
                print("---------------------------------------")
        case 4:
            if  not titulos:
                print("-------------------------------")
                print("NO Hay titulos cargador todavia")
                print("-------------------------------")
            else:
                print("-----Consultar disponibilidad-------")
                buscar=input("Titulo: ").strip().capitalize()
                if buscar in titulos:
                    print(f"{buscar} tiene {ejemplares[titulos.index(buscar)]}")
                else:
                    print("No se encuentra en la base de datos")
        case 5:
            if  not titulos:
                print("-------------------------------")
                print("NO Hay titulos cargador todavia")
                print("-------------------------------")
            else:
                bandera=0
                print("------------------------------------")
                for contador in range(len(titulos)):
                    if ejemplares[contador]==0:
                        print(f"* {titulos[contador]} tiene {ejemplares[contador]} ejemplares")
                        bandera +=1
                if bandera ==0:
                    print("------------------------------------")
                    print("Todos los Titulos tienen ejemaplares")
                    print("------------------------------------")
                print("------------------------------------")
        case 6:
            if  not titulos:
                print("-------------------------------")
                print("NO Hay titulos cargador todavia")
                print("-------------------------------")
            else:
                print("------------Agregar titulos------------")
                nuevo=input("Ejemplar nuevo: ").strip().capitalize()
                titulos.append(nuevo)
                while True:
                         nuevo_ejemplar=input("Cantidad: ").strip()
                         if not nuevo_ejemplar.isdigit() or nuevo_ejemplar=="":
                             print("Ingreso un valor erroneo, intente nuevamente")
                         else:
                            nuevo_ejemplar=int(nuevo_ejemplar)
                            ejemplares.append(nuevo_ejemplar)
                            break
                print("----------------------------------------")
        case 7:
            if  not titulos:
                print("-------------------------------")
                print("NO Hay titulos cargador todavia")
                print("-------------------------------")
            else:
                print("--------Prestamao / Devoluciones------------")
                actualizar=input("Titulo: ").strip().capitalize()
                if actualizar in titulos:
                    bandera=True
                    while bandera:
                        opcion=input("\n1-Prestamo \n2-Devolucion \nOpcion: ").strip()
                        if not opcion.isdigit() or opcion=="":
                            print("Ingreso un valor erroneo, intente de nuevo")
                        else:
                            opcion=int(opcion)
                            match opcion:
                                case 1:
                                    if ejemplares[titulos.index(actualizar)]==0:
                                        print("No puede pedir mas prestamos, tiene cero ejemplares")
                                    else:                                        
                                        while True:
                                            prestamo=input("Cantidad: ").strip()
                                            if not prestamo.isdigit() or prestamo=="":
                                                print("Ingreso un valor erroneo, intente de nuevo")
                                                continue
                                            else:
                                                prestamo=int(prestamo)
                                                if  prestamo < ejemplares[titulos.index(actualizar)] :
                                                    ejemplares[titulos.index(actualizar)]-= prestamo
                                                    bandera=False
                                                    break
                                                else:
                                                    ejemplares[titulos.index(actualizar)]=0 
                                                    bandera=False
                                                    break                                            
                                case 2:
                                    while True:                                        
                                        regreso=input("Cuanto devuelve: ").strip()
                                        if not regreso.isdigit() or regreso=="":
                                            print("Ingreso un valor errones, intente de nuevo")
                                            continue
                                        else:
                                            regreso=int(regreso)
                                            ejemplares[titulos.index(actualizar)] += regreso
                                            bandera=False
                                            break
                                case _:
                                    print("Error") 
                                    bandera=False
                                    break
                            bandera=False
            print("--------------------------------------------")
        case 8:
            print("Cierre del programa")
            break
        case _:
            print("Selecciono un valor que no corresponde")   
