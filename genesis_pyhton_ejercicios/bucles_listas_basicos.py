# Ejercicios Básicos con Listas y Bucles
# for 1.
# Calcula el factorial de un número ingresado por el usuario utilizando un bucle
# for
n = int(input("Tirá un número para sacar el factorial: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("El factorial es:", factorial)

# 2.
# Genera una secuencia de Fibonacci hasta un número ingresado por el usuario utilizandoun bucle
# for
limite = int(input("¿Hasta qué número querés la serie Fibonacci?: "))
a, b = 0, 1

print(a, end=" ")

for _ in range(limite - 1):
    print(b, end=" ")
    a, b = b, a + b


# 3.
# Pide al usuario un número y genera una lista con los primeros N números naturalesusando un bucle
# for
n = int(input("¿Cuántos números naturales querés?: "))
naturales = []

for i in range(1, n + 1):
    naturales.append(i)

print(naturales)

# 4.
# Solicita una lista de números y muestra la suma de los números usando un bucle
# for
numeros = input("Tirá números separados por coma: ").split(",")
numeros = list(map(int, numeros))
suma = 0

for num in numeros:
    suma += num

print("La suma es:", suma)


# 5.
# Usa un bucle for para encontrar el número máximo en una lista de números ingresadapor el usuario.

numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
maximo = numeros[0]

for num in numeros:
    if num > maximo:
        maximo = num

print("El número más grande es:", maximo)

# 6.
# Genera una lista con los cuadrados de los primeros 10 números naturales usando unbucle
# for
cuadrados = []

for i in range(1, 11):
    cuadrados.append(i ** 2)

print(cuadrados)

# 7.
# Pide una lista de palabras y cuenta cuántas palabras tienen más de 5 letras utilizando unbucle
# for
palabras = input("Tirá palabras separadas por espacio: ").split()
contador = 0

for palabra in palabras:
    if len(palabra) > 5:
        contador += 1

print("Palabras con más de 5 letras:", contador)

# 8.
# Usando un bucle
# for cuenta cuántas veces aparece una palabra específica en una listade palabras.
palabras = input("Tirá palabras separadas por espacio: ").split()
buscar = input("¿Qué palabra querés buscar?: ")
contador = 0

for palabra in palabras:
    if palabra == buscar:
        contador += 1

print(f"La palabra '{buscar}' aparece {contador} veces.")

# 9.
# Solicita una lista de números y calcula su promedio usando un bucle
# for
numeros = input("Tirá números separados por coma: ").split(",")
numeros = list(map(int, numeros))
suma = 0

for num in numeros:
    suma += num

promedio = suma / len(numeros)
print("El promedio es:", promedio)

# 10.
# Usa un bucle for para eliminar los elementos duplicados de una lista de números.
numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
sin_duplicados = []

for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Lista sin duplicados:", sin_duplicados)

# 11.
# Crea una lista con los primeros 10 números multiplicados por 2 usando un bucle
# for
multiplicados = []

for i in range(1, 11):
    multiplicados.append(i * 2)

print(multiplicados)


# 12.
# Pide al usuario que ingrese una lista de números y usa un bucle for para imprimir cadanúmero multiplicado por 5.
numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))

for num in numeros:
    print(num * 5)




# 13.
# Usa un bucle
# for para contar cuántos números en una lista son mayores que 10.
numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
contador = 0

for num in numeros:
    if num > 10:
        contador += 1

print("Números mayores que 10:", contador)

# 14.
# Pide una lista de palabras y usa un bucle
# for para imprimir las palabras en orden inverso.
palabras = input("Tirá palabras separadas por espacio: ").split()

for palabra in palabras[::-1]:
    print(palabra)

# 15.
# Genera una lista con los primeros 20 números divisibles por 3 usando un bucle
# for
divisibles = []
i = 1

for num in range(1, 100):
    if num % 3 == 0:
        divisibles.append(num)
    if len(divisibles) == 20:
        break

print(divisibles)

# 16.
# Usa un bucle
# for
# para imprimir los elementos de una lista de cadenas en minúsculas.

palabras = input("Tirá palabras separadas por espacio: ").split()

for palabra in palabras:
    print(palabra.lower())

# 17.
# Crea una lista con los primeros 5 números elevados al cubo usando un bucle
# for
cubos = []

for i in range(1, 6):
    cubos.append(i ** 3)

print(cubos)





# 18.
# Pide una lista de números y usa un bucle
# for
# para mostrar solo los números negativos.

numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))

for num in numeros:
    if num < 0:
        print(num)

# 19.
# Usa un bucle
# for
# para contar cuántas veces aparece un número específico en una lista denúmeros.
numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
buscar = int(input("¿Qué número querés buscar?: "))
contador = 0

for num in numeros:
    if num == buscar:
        contador += 1

print(f"El número {buscar} aparece {contador} veces.")

# 20.
# Crea una lista con los primeros 10 números impares usando un bucle
# for
impares = []

for i in range(1, 20, 2):
    impares.append(i)

print(impares)
