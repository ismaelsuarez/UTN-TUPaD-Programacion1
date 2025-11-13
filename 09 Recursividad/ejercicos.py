# Recursividad en Python
# Guía de Ejercicios - Técnicas de Programación Recursiva

# ============================================================================
# EJEMPLOS BÁSICOS DE RECURSIVIDAD
# ============================================================================

# 1) Cuenta regresiva (ejemplo simple de recursividad)
# Caso base: cuando n == 0, imprime "¡Despegue!"
# Paso recursivo: imprime n y llama a la función con n-1
def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)


# 2) Suma de elementos de una lista
# Caso base: lista vacía retorna 0
# Paso recursivo: suma el primer elemento con la suma del resto de la lista
def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


# ============================================================================
# EJEMPLOS CLÁSICOS DE RECURSIVIDAD
# ============================================================================

# 3) Factorial recursivo
# Caso base: factorial(0) = 1 y factorial(1) = 1
# Paso recursivo: factorial(n) = n × factorial(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def imprimir_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")


# 4) Serie de Fibonacci recursiva
# Caso base: fibonacci(0) = 0, fibonacci(1) = 1
# Paso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def imprimir_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")


# ============================================================================
# EJERCICIOS ADICIONALES DE RECURSIVIDAD
# ============================================================================

# 5) Potencia recursiva
# Caso base: cualquier número elevado a 0 es 1
# Paso recursivo: base^exponente = base × base^(exponente-1)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# 6) Conversión decimal a binario
# Caso base: cuando n == 0, retorna cadena vacía
# Paso recursivo: convierte n//2 y concatena el resto (n % 2)
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    return decimal_a_binario(n) if n != 0 else "0"


# 7) Verificar si una palabra es palíndromo
# Caso base: palabra vacía o de 1 carácter es palíndromo
# Paso recursivo: compara primer y último carácter, luego verifica el resto
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


# 8) Suma de dígitos de un número
# Caso base: número de un solo dígito, retorna el número
# Paso recursivo: suma el último dígito con la suma de los dígitos restantes
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


# 9) Contar bloques en una pirámide
# Caso base: pirámide de 1 nivel tiene 1 bloque
# Paso recursivo: nivel n tiene n bloques + bloques de nivel n-1
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


# 10) Contar cuántas veces aparece un dígito en un número
# Caso base: número 0, no hay más dígitos que contar
# Paso recursivo: verifica si el último dígito coincide y suma al conteo del resto
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)


if __name__ == "__main__":
    print("=" * 60)
    print("EJEMPLOS BÁSICOS DE RECURSIVIDAD")
    print("=" * 60)
    
    print("\n1. Cuenta regresiva desde 5:")
    cuenta_regresiva(5)
    
    print("\n2. Suma de lista [1, 2, 3, 4]:", suma_lista([1, 2, 3, 4]))
    
    print("\n" + "=" * 60)
    print("EJEMPLOS CLÁSICOS")
    print("=" * 60)
    
    print("\n3. Factoriales hasta 5:")
    imprimir_factoriales(5)

    print("\n4. Fibonacci hasta posición 7:")
    imprimir_fibonacci(7)
    
    print("\n" + "=" * 60)
    print("EJERCICIOS ADICIONALES")
    print("=" * 60)

    print("\n5. Potencia 2^5:", potencia(2, 5))

    print("\n6. Binario de 10:", convertir_a_binario(10))

    print("\n7. ¿'reconocer' es palíndromo?", es_palindromo("reconocer"))

    print("\n8. Suma de dígitos de 1234:", suma_digitos(1234))

    print("\n9. Bloques para pirámide de base 4:", contar_bloques(4))

    print("\n10. Cantidad de veces que aparece el 2 en 12233421:", contar_digito(12233421, 2))
