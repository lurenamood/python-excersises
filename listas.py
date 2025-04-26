# Enunciados sobre Listas, Input, Casteo yCondicionales

# 1.
# Solicita al usuario que ingrese un número y agrégalo a una lista.


def agregar_numero():
    lista = []
    num = int(input("Escribe un número para agragarlo en la lista: "))
    lista.append(num)
    print("Así quedó la lista:", lista)

agregar_numero()


# 2.
# Pide al usuario que ingrese un número y agrega ese número al final de la lista.
def agregar_final():
    lista = [5, 10, 15]
    num = int(input("Escribe un número para agregarlo al final: "))
    lista.append(num)
    print("Lista actualizada:", lista)

agregar_final()

# 3.
# Solicita una lista de números al usuario e imprime el primer número de la lista.
def mostrar_primero():
    lista = list(map(int, input("Escribe números separados por espacio: ").split()))
    if lista:
        print("Este fue el primero:", lista[0])
    else:
        print("No has ouesto nada.")

mostrar_primero()


# 4.
# Solicita al usuario que ingrese un número y elimina ese número de una lista si existe.
def sacar_numero():
    lista = [3, 6, 9, 12]
    print("Mira la lista:", lista)
    num = int(input("¿Qué número querés sacar?: "))
    if num in lista:
        lista.remove(num)
        print("Ya estuvo, quedó así:", lista)
    else:
        print("Ese número ni estaba.")

sacar_numero()



# 5.
# Pide una lista de números al usuario e imprime el último número de la lista.
def mostrar_ultimo():
    lista = list(map(int, input("Escribe tus números: ").split()))
    if lista:
        print("El último que diste fue:", lista[-1])
    else:
        print("No Tienes nada.")

mostrar_ultimo()


# 6.
# Solicita al usuario una lista de palabras y agrega una palabra al principio de la lista.
def agregar_principio():
    palabras = input("Decime unas palabras: ").split()
    nueva = input("Colocar una palabra para agragarlo al principio: ")
    palabras.insert(0, nueva)
    print("Lista nueva:", palabras)

agregar_principio()



# 7.
# Pide una lista de números y muestra la longitud de la lista.
def contar_elementos():
    lista = list(map(int, input("Envíame varios números: ").split()))
    print(f"Tienes {len(lista)} números.")

contar_elementos()


# 8.
# Solicita al usuario una lista de palabras y muestra si una palabra específica está en la lista.
def buscar_palabra():
    palabras = input("Ingresa algunas palabras: ").split()
    buscar = input("¿Qué palabra querés buscar?: ")
    if buscar in palabras:
        print(f"Sí, '{buscar}' está.")
    else:
        print(f"No está '{buscar}' en la lista.")

buscar_palabra()
# 9.
# Solicita al usuario que ingrese una lista de números y muestra si la lista está vacía.
def verificar_lista():
    numeros = list(map(int, input("Escribe números (o nada si quieres): ").split()))
    if numeros:
        print("La lista tiene algo.")
    else:
        print("Vacía.")

verificar_lista()






# 10.
# Solicita al usuario que ingrese un número y lo agrega a la lista, luego imprime la lista.
def agregar_y_mostrar():
    lista = []
    num = int(input("Ingresa un número: "))
    lista.append(num)
    print("Así va quedando:", lista)

agregar_y_mostrar()





# 11.
# Pide una lista de números al usuario y muestra el primer número mayor que 10.
def mayor_que_diez():
    numeros = list(map(int, input("Escribe tus números: ").split()))
    for n in numeros:
        if n > 10:
            print("Este fue el primero mayor que 10:", n)
            break
    else:
        print("Ninguno pasó de 10.")

mayor_que_diez()




# 12.
# Solicita una lista de números y convierte la lista a una cadena de texto con comas.
def lista_a_cadena():
    numeros = list(map(int, input("Escribir números: ").split()))
    cadena = ', '.join(map(str, numeros))
    print("Así quedó la lista en texto:", cadena)

lista_a_cadena()




# 13.
# Solicita al usuario una lista de números y muestra el mayor número.
def numero_mayor():
    numeros = list(map(int, input("Escribir números: ").split()))
    if numeros:
        print("El mas es:", max(numeros))
    else:
        print("No metiste nada.")

numero_mayor()




# 14.
# Pide una lista de palabras al usuario y convierte la lista a una tupla.
def palabras_a_tupla():
    palabras = input("Dime unas palabras: ").split()
    tupla = tuple(palabras)
    print("Aquí está la tupla:", tupla)

palabras_a_tupla()


# 15.
# Solicita una lista de números y elimina todos los números negativos.
def quitar_negativos():
    numeros = list(map(int, input("Escribir números: ").split()))
    positivos = [n for n in numeros if n >= 0]
    print("Solo positivos quedaron:", positivos)

quitar_negativos()


# 16.
# Solicita una lista de números y convierte la lista a un conjunto.
def lista_a_conjunto():
    numeros = list(map(int, input("Escribir números: ").split()))
    conjunto = set(numeros)
    print("Aquí el conjunto:", conjunto)

lista_a_conjunto()

# 17.
# Pide una lista de números al usuario e imprime los números en orden descendente.
def ordenar_descendente():
    numeros = list(map(int, input("Escribe tus números: ").split()))
    numeros.sort(reverse=True)
    print("Ordenados de mayor a menor:", numeros)

ordenar_descendente()



# 18.
# Solicita una lista de palabras y muestra el tipo de datos de la lista.
def tipo_de_lista():
    palabras = input("Ingresa palabras: ").split()
    print("Este es el tipo:", type(palabras))

tipo_de_lista()


# 19.
# Pide al usuario que ingrese un número y agrega ese número a una lista si no está ya presente.
def agregar_si_no_esta():
    lista = []
    num = int(input("Pon un número: "))
    if num not in lista:
        lista.append(num)
        print("Ya lo agregué:", lista)
    else:
        print("Ese número ya estaba.")

agregar_si_no_esta()



# 20.
# Solicita una lista de palabras al usuario y muestra la palabra más corta.
def palabra_mas_corta():
    palabras = input("Tirá palabras: ").split()
    if palabras:
        corta = min(palabras, key=len)
        print("La más chiquita es:", corta)
    else:
        print("No pusiste nada.")

palabra_mas_corta()
