# El reto:
 #Vamos a crear un programa que:
 #1.Solicite números al usuario hasta que ingrese cero
 #2.Para cada número, muestre la suma de sus dígitos
 #3.Al finalizar, muestre la sumatoria total y la suma de dígito
 

def suma(numero):
    suma=numero+suma
    return suma

def total(numero_total):
    total=numero_total
    return total



entrada=True
while entrada:
    numero_sumar=int(input("Numero a sumar: "))
    if numero_sumar==0:
        entrada=False
        break
    suma(numero_sumar)
    
    total(numero_sumar)
print(f"La suma de los numeros es {suma} y la sumatoria total es {total}")

