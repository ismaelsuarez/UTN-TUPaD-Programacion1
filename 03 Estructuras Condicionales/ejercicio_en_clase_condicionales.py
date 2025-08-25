
# Si el usuario ingresa un día de la semana inexistente o 
# una fecha cuyo día supere el número 31 o el mes supere el número 12, 
# finalizar el programa indicando que se produjo un error.
#*Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los exámenes,
#*pero eso solo si se trata de los niveles inicial, intermedio o avanzado*,
#*prácticas habladas y el inglés para viajeros no tienen exámenes*.

#*Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el programa le mostrará el porcentaje de aprobados. 
#*Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa 
#*le indicará ‘asistió la mayoría’ en caso de que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ 
#*si no es así. 
#*Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir 
# ‘Comienzo de nuevo ciclo’ y 
# solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.


print('----------------------')
fecha=input("Ingrese dia de la semana, dd: para numero de dia y mm: para el mes " \
"(Ejemplo: lunes,15,3): ")
dia, dd, mm=fecha.split(',')
dd=int(dd)
mm=int(mm)
print('----------------------')
if (not(dia.lower() == 'domingo' or dia.lower()=='sabado'or (dd >= 29 and mm == 2) or (dd >= 31 and mm == 4 or mm == 6 or mm == 9 or mm == 11) or mm <= 12)):
    print("El dia ingresado es inexistente")
else:
    
    if dia.lower()=='lunes' or dia.lower()=='martes' or dia.lower()=='miercoles':
        aprobados=int(input('Cuantos aprobaron: '))
        desaprobados=int(input('Cuantos desaprobado: '))
        cantidad_alumnos=aprobados+desaprobados
        porcentaje=(aprobados / cantidad_alumnos) * 100
        print("El porcentaje de aprobado es: ", porcentaje)

    elif dia.lower()=='jueves':
        porcentaje_hablada=int(input('Porcentaje de ingresados: '))
        if porcentaje_hablada >=50:
            print('Asistio la mayoria')
        else:
            print('No asistio la mayoria')
        pass

    if dia.lower()=='viernes' and dd == 1 and mm == 1 or mm == 7:
        print('Comienzo de nuevo ciclo')
        inreso_nuevo=input('Ingrese  la cantidad de alumnos y el arancel por alumno ejemplo (20,1500): ')
        alumnos, arancel=inreso_nuevo.split(",")
        alumnos=int(alumnos)
        arancel=int(arancel)
        total_arancel=alumnos*arancel
        print(f'El total de ingreso en: $ {total_arancel}')
    print('----------------------')


