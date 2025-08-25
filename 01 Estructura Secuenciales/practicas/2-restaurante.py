#Calculadora de propinas en un restaurante 
#Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el 
#monto de la cuenta. 
#El programa debe: 
#✓ Pedir al usuario el monto total de la cuenta. 
#✓ Calcular la propina sugerida al 10%. 
#✓ Calcular la propina sugerida al 15%. 
#✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
#✓ Mostrar todos los resultados en pantalla.

print("------------------------------")
print("Bienvenido al restaurante Tito")
print("------------------------------")
print(" ")
cuenta=int(input("Por favor ingrese el valor total de la cuenta "))
porcentaje_10=cuenta/100 *10
total_a_pagar_con_el_10=cuenta+porcentaje_10
porcentaje_15=cuenta/100 *15
total_a_pagar_con_el_15=cuenta+porcentaje_15
print(f"Propina sugerida 10% :{porcentaje_10}")
print(f"Total a pagar con el 10% : {total_a_pagar_con_el_10}")
print(f"Propina sugerida 15% : {porcentaje_15}")
print(f"Total a pagar con el 25% : {total_a_pagar_con_el_15}")
