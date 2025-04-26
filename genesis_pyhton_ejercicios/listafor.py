# 1.
# Solicita al usuario que ingrese una lista de números separados por comas, convierte esa entradaa una lista y muestra la suma de los números.
numeros = input("Tirá números separados por comas: ").split(",")
numeros = list(map(int, numeros))
print("La suma de los números es:", sum(numeros))



# 2.
# Pide al usuario ingresar varios números separados por espacios y convierte la entrada en unalista de enteros, luego muestra el número mayor.
numeros = input("Coloca números separados por espacio: ").split()
numeros = list(map(int, numeros))
print("El número mayor es:", max(numeros))


# 3.
# Solicita al usuario que ingrese una lista de palabras y convierte la entrada en una lista. Luego,imprime el número de palabras en la lista.
palabras = input("colocar palabras separadas por espacio: ").split()

print("Cantidad de palabras:", len(palabras))


# 4.
# Pide al usuario una lista de edades (separadas por comas) y calcula el promedio de las edades.
edades = input("Colocar edades separadas por comas: ").split(",")
edades = list(map(int, edades))
promedio = sum(edades) / len(edades)
print("Promedio de edades:", promedio)



# 5.
# Solicita una lista de números y muestra cuántos de esos números son positivos.
numeros = input("Colocar números separados por comas: ").split(",")
numeros = list(map(int, numeros))
positivos = [n for n in numeros if n > 0]
print("Cantidad de positivos:", len(positivos))


# 6.
# Pide al usuario que ingrese una lista de enteros separados por espacios y muestra el númeromás pequeño de la lista.
numeros = input("Colocar enteros separados por espacio: ").split()
numeros = list(map(int, numeros))
print("El número más pequeño es:", min(numeros))





# 7.
# Solicita una lista de números y devuelve solo los números impares.
numeros = input("Tirá tus números: ").split()
numeros = list(map(int, numeros))
impares = [n for n in numeros if n % 2 != 0]
print("Números impares:", impares)



# 8.
# Pide al usuario que ingrese una lista de números y muestra los que son divisibles por 2 y 3.
numeros = input("Colocar números separados por espacio: ").split()
numeros = list(map(int, numeros))
divisibles = [n for n in numeros if n % 2 == 0 and n % 3 == 0]
print("Números divisibles entre 2 y 3:", divisibles)



# 9.
# Solicita una lista de palabras y devuelve la palabra más larga.
palabras = input("Colocar palabras separadas por espacio: ").split()
larga = max(palabras, key=len)
print("La palabra más larga es:", larga)
# 10.
# Pide al usuario una lista de números y muestra la cantidad de números negativos en la lista.
numeros = input("Pon números separados por espacio: ").split()
numeros = list(map(int, numeros))
negativos = [n for n in numeros if n < 0]
print("Cantidad de negativos:", len(negativos))



# Nivel 2: Intermedio (Condicionales y Casting)
# 11.
# Solicita una lista de números, conviértela a una lista de enteros y muestra los números mayores a10.
numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
mayores_diez = [n for n in numeros if n > 10]
print("Números mayores a 10:", mayores_diez)



# 12.
# Pide una lista de números al usuario, conviértela a una lista de enteros, y muestra solo losnúmeros mayores a un número específico introducido por el usuario.

numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
limite = int(input("¿Mostrame los números mayores a cuánto?: "))
mayores = [n for n in numeros if n > limite]
print(f"Números mayores a {limite}:", mayores)


# 13.
# Solicita una lista de palabras y devuelve la lista sin las palabras que tengan menos de 4caracteres.
palabras = input("Tirá palabras separadas por espacio: ").split()
largas = [p for p in palabras if len(p) >= 4]
print("Palabras de 4 letras o más:", largas)



# 14.
# Pide al usuario que ingrese una lista de números y muestra solo aquellos que sean mayores que0 y menores que 100.
numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
entre_cero_cien = [n for n in numeros if 0 < n < 100]
print("Números entre 0 y 100:", entre_cero_cien)


# 15.
# Solicita una lista de edades de personas (en formato de cadena), conviértela a enteros y muestrael promedio de las edades de las personas mayores de 18 años.
edades = input("Tirá edades separadas por coma: ").split(",")
edades = list(map(int, edades))
mayores = [e for e in edades if e > 18]
if mayores:
    promedio_mayores = sum(mayores) / len(mayores)
    print("Promedio de mayores de edad:", promedio_mayores)
else:
    print("No hay mayores de edad.")



# 16.
# Pide una lista de números y muestra cuántos de esos números son divisibles entre 5.

numeros = input("Tirá números separados por espacio: ").split()
numeros = list(map(int, numeros))
divisibles_cinco = [n for n in numeros if n % 5 == 0]
print("Números divisibles entre 5:", divisibles_cinco)
