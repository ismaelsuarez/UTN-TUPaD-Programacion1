tarjeta = []
saldos = []

while True:
    print("")
    print("********************MENU********************")
    print("1.Ingresar números de tarjeta \n2.Ingresar saldos correspondientes \n3.Mostrar todas las tarjetas y saldos",
          "\n4.Consultar saldo por número \n5.Listar saldos en negativo o cero \n6.Agregar tarjeta \n7.Ver saldos ≤ 0",
          "\n8.Cargar/debitar saldo \n9.Ver todas \n10.Salir")
    opcion = input("Opcion: ").strip()
    if not opcion.isdigit() or opcion=="":
        print("-----------Error-------------")
        print("🛑 Ingrese un numero valido")
        print("-----------Error-------------")
        continue
    opcion=int(opcion)
    match opcion:
        case 1:
            print("-------Ingreso de tarjeta-------")
            cantidad_ingreso = int(input("Cuantos, va ingresar: "))
            for contador in range(cantidad_ingreso):
                nuevo = int(input("Numero: "))
                tarjeta.append(nuevo)
                saldos.append(0)
            print("--------------------------------")
        case 2:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("-------Ingreso saldo------------")
                for contador in range(len(tarjeta)):
                    saldo = int(input(f"Saldo para {tarjeta[contador]}: "))
                    saldos[contador] = saldo
        case 3:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("------------Saldos--------------")
                for contador in range(len(tarjeta)):
                    print(f"Tarjeta N°: {tarjeta[contador]} saldo: {saldos[contador]}")
                print("--------------------------------")
        case 4:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("------Consultar saldo-----------")
                respuesta = int(input("Numero: "))
                if respuesta in tarjeta:
                    print(f"Targeta {respuesta} saldo: {saldos[tarjeta.index(respuesta)]}")
                print("--------------------------------")
        case 5:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("\n1-Saldo positivo \n2-Saldo negativo")
                opcion=int(input("Opcion: "))
                match opcion:
                    case 1:
                        print("------Saldo Positivo------------")
                        for contador in range(len(tarjeta)):
                            if saldos[contador]>0:
                                print(f"Tarjeta:{tarjeta[contador]} su saldo: {saldos[contador]}")
                        print("--------------------------------")
                    case 2: 
                        print("------Saldo Negativo------------")
                        for contador in range(len(tarjeta)):
                            if saldos[contador]<=0:
                                print(f"Tarjeta:{tarjeta[contador]} su saldo: {saldos[contador]}")
                        print("--------------------------------")
                    case _:
                        print("--------------------------")
                        print("Debe ingresar entre 1 o 2")
                        print("--------------------------")
        case 6:
            print("---------------Cargar nueva tarjeta---------------")
            nueva_tarjeta=int(input("Tarjeta: "))
            tarjeta.append(nueva_tarjeta)
            nuevo_saldo=int(input("Saldo: "))
            saldos.append(nuevo_saldo)
            print("--------------------------------------------------")
            
        case 7:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("------Saldo Negativo------------")
                for contador in range(len(tarjeta)):
                    if saldos[contador]<=0:
                        print(f"Tarjeta:{tarjeta[contador]} su saldo: {saldos[contador]}")
                print("--------------------------------")
        case 8:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("--------Cargar o Debitar saldo-----------")
                respuesta = int(input("Tarjeta Numero: "))                
                if respuesta in tarjeta:
                    opcion=int(input("\n1-Cargar saldo \n2-Debitar saldo \nRepuesta: "))
                    match opcion:
                        case 1:
                            print("------Cargar Saldo------")  
                            cargar=int(input("Saldo a cargar: "))                            
                            saldos[tarjeta.index(respuesta)]+=cargar
                        case 2:
                            print("------Debitar Saldo------")  
                            debitar=int(input("Saldo a debitar: "))
                            saldos[tarjeta.index(respuesta)]-=debitar
                else:
                    print("🛑 No hay tarjeta cargada con ese numero")
                print("--------------------------------")
        case 9:
            if not tarjeta:
                print("----------------------")
                print("🛑 No hay tarjetas cargadas")
                print("----------------------")
            else:
                print("------------Saldos--------------")
                for contador in range(len(tarjeta)):
                    print(f"Tarjeta N°: {tarjeta[contador]} saldo: {saldos[contador]}")
                print("--------------------------------")
        case 10:
            print("Cierre del programa-Hasta mañana")
            break
        case _:
            print("----------------------------------")
            print("Debe ingresar un numero del 1 al 9")
            print("----------------------------------")
