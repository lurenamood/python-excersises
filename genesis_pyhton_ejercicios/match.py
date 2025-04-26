        
# Ejercicios para usar match con datos primitivos en Python
#  1. Ejercicio 1: Identificar el tipo de dato
#  Solicita al usuario que ingrese un valor (puede ser un número entero, flotante, un booleano o una
#  cadena). Luego, usa match para identificar el tipo de dato ingresado y muestra un mensaje
#  correspondiente. Por ejemplo, si el valor es un número entero, muestra "Es un entero", si es un flotante,
#  muestra "Es un número decimal", etc.



#  2. Ejercicio 2: Identificar la estación del año
#  Dado un número del 1 al 12 que representa un mes, usa match para identificar en qué estación del año
#  cae. Los meses 1-3 corresponden a "Invierno", 4-6 a "Primavera", 7-9 a "Verano" y 10-12 a "Otoño".
#  Muestra la estación correspondiente según el mes ingresado.
mes = int(input("Ingresa un número del 1 al 12 para saber la estación del año: "))

match mes:
    case 1 | 2 | 3:
        print("Es Invierno.")
    case 4 | 5 | 6:
        print("Es Primavera.")
    case 7 | 8 | 9:
        print("Es Verano.")
    case 10 | 11 | 12:
        print("Es Otoño.")
    case _:
        print("Número de mes inválido.")
        
        
#  3. Ejercicio 3: Evaluar un valor booleano
#  Usa match para verificar si un valor booleano es True o False, y muestra un mensaje personalizado
#  para cada caso. Si el valor es True, muestra "¡Correcto!", y si es False, muestra "¡Incorrecto!".
valor_booleano = input("Ingresa un valor booleano (True/False): ")

valor_booleano = valor_booleano.lower() == "true"

match valor_booleano:
    case True:
        print("¡Correcto!")
    case False:
        print("¡Incorrecto!")



#  4. Ejercicio 4: Verificar el rango de una edad
#  Pide al usuario que ingrese su edad y utiliza match para categorizar a la persona según su edad. Los
#  rangos son los siguientes:
#  0-12 años: "Niño"
#  13-17 años: "Adolescente"
#  18-64 años: "Adulto"
#  65 o más años: "Anciano"



edad = int(input("Ingresa tu edad: "))

match edad:
    case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
        print("Niño")
    case 13 | 14 | 15 | 16 | 17:
        print("Adolescente")
    case 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64:
        print("Adulto")
    case _ if edad >= 65:
        print("Anciano")

#  5. Ejercicio 5: Identificar el signo de un número
#  Dado un número (positivo, negativo o cero), utiliza match para identificar su signo y mostrar un mensaje
#  correspondiente. Si el número es positivo, muestra "Es un número positivo", si es negativo, muestra "Es
#  un número negativo", y si es cero, muestra "Es cero".
numero = float(input("Ingresa un número: "))

match True:
    case numero if numero > 0:
        print("Es un número positivo.")
    case numero if numero < 0:
        print("Es un número negativo.")
    case _:
        print("Es cero.")



#  Ejercicios para usar expresiones en Python



#  1. Ejercicio 1: Evaluar si un número es par o impar
#  Solicita al usuario que ingrese un número entero y usa una expresión para verificar si el número es par o
#  impar. Si el número es par, muestra "Es par", si es impar, muestra "Es impar".ç
numero = int(input("Ingresa un número entero: "))

print("Es par" if numero % 2 == 0 else "Es impar")



#  2. Ejercicio 2: Verificar si un número es mayor que 10 y menor que 50
#  Pide al usuario que ingrese un número y utiliza una expresión para verificar si el número es mayor que 10
#  y menor que 50. Muestra un mensaje correspondiente: "El número está en el rango" o "El número no está
# en el rango".
numero = int(input("Ingresa un número: "))
print("El número está en el rango" if 10 < numero < 50 else "El número no está en el rango")



#  3. Ejercicio 3: Verificar si una palabra es palíndroma
#  Pide al usuario que ingrese una palabra y utiliza una expresión para verificar si la palabra es un
#  palíndromo. Una palabra es palíndroma si se lee igual de izquierda a derecha que de derecha a
#  izquierda. Muestra el mensaje "Es un palíndromo" o "No es un palíndromo".



#  4. Ejercicio 4: Evaluar si una persona es mayor de edad
#  Solicita al usuario su edad y usa una expresión para verificar si es mayor de edad (18 años o más). Si lo
#  es, muestra "Eres mayor de edad", si no lo es, muestra "Eres menor de edad".
edad = int(input("Ingresa tu edad: "))

print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")


#  5. Ejercicio 5: Calcular el área de un triángulo
#  Solicita al usuario que ingrese la base y la altura de un triángulo, y utiliza una expresión para calcular el
#  área utilizando la fórmula: Área = (base * altura) / 2. Muestra el resultado del área calculada
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2
print(f"El área del triángulo es: {area}")
