# Ejercicios sobre
#  Condicionales en Python
#  Ejercicio 1
#  Dada una edad ingresada por el usuario, determina si es mayor de edad (18 o más) o menor de edad (menos de 18).
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad < 18:
    print("Eres menor de edad.")
    
    
    
    

# Ejercicio 2
#  Pide al usuario que ingrese un número de tres dígitos. Imprime si es un número par o impar.
numero = int(input("Por favor, ingresa un número de tres dígitos: "))

if 100 <= abs(numero) <= 999:
    
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
else:
    print("El número ingresado no tiene tres dígitos.")
    

# Ejercicio 3
#  Un usuario ingresa un salario mensual. Si el salario es mayor o igual a $2000, imprime "Salario alto", si es menor a
#  $2000 pero mayor a $1000, imprime "Salario medio", y si es menor a $1000, imprime "Salario bajo".



# Ejercicio 4
#  Solicita un número entre 1 y 12 al usuario e imprime el nombre del mes correspondiente.



# Ejercicio 5
#  Un estudiante ingresa su puntaje en un examen. Si el puntaje es mayor o igual a 90, imprime "Aprobado con Distinción".
#  Si es mayor o igual a 70 pero menor a 90, imprime "Aprobado". Si es menor a 70, imprime "Reprobado".
puntaje = int(input("Por favor, ingresa tu puntaje en el examen: "))

if puntaje >= 90:
    print("Aprobado con Distinción")
elif puntaje >= 70 and puntaje <= 90:
    print("Aprobado")
else:
    print("Reprobado")
    

# Ejercicio 7
#  Ingresa un valor numérico para representar una temperatura en grados Celsius y determina si está bajo cero, entre 0 y
#  30 grados, o por encima de 30 grados.
temperatura = float(input("Ingresa la temperatura en grados Celsius: "))

if temperatura < 0:
    print("Está bajo cero.")
elif 0 <= temperatura <= 30:
    print("Está entre 0 y 30 grados.")
else:
    print("Está por encima de 30 grados.")

# Ejercicio 8
#  Si un número ingresado por el usuario es mayor que 100, imprímelo dividido entre 2. Si es menor o igual a 100,
#  imprímelo multiplicado por 2.

numero = float(input("Ingresa un número: "))

if numero > 100:
    print(numero / 2)
else:
    print(numero * 2)

# Ejercicio 9
#  Un alumno introduce las horas de trabajo semanal. Si las horas son más de 40, imprime "Trabajo a tiempo completo", si
#  son menos de 40, imprime "Trabajo a medio tiempo".
  
horas = int(input("Ingresa las horas de trabajo semanal: "))

if horas > 40:
    print("Trabajo a tiempo completo")
else:
    print("Trabajo a medio tiempo")

# Ejercicio 10
#  Pide la edad y determina si es un niño (menor de 12), un adolescente (entre 12 y 18), un adulto joven (entre 19 y 30), si
#  es un adulto (mayor de 30) o si es persona perteneciente al a tercera edad(65)

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Niño")
elif 12 <= edad <= 18:
    print("Adolescente")
elif 19 <= edad <= 30:
    print("Adulto joven")
elif edad > 30 and edad < 65:
    print("Adulto")
else:
    print("Persona de la tercera edad")


# Ejercicio 11
#  Solicita un número de calificación entre 0 y 10. Si la calificación es mayor o igual a 9, imprime "Excelente". Si es mayor o
#  igual a 7 pero menor a 9, imprime "Bueno". Si es menor a 7, imprime "Necesita mejorar".
 
 
calificacion = float(input("Ingresa la calificación (0 a 10): "))

if calificacion >= 9:
    print("Excelente")
elif 7 <= calificacion < 9:
    print("Bueno")
else:
    print("Necesita mejorar")


# Ejercicio 12
#  Pide al usuario que ingrese un número. Si el número es mayor que 50, imprime su mitad. Si es menor o igual a 50,
#  imprímelo multiplicado por 3.
numero = float(input("Ingresa un número: "))

if numero > 50:
    print(numero / 2)
else:
    print(numero * 3)

# Ejercicio 13
#  Solicita al usuario que ingrese un valor en minutos y determina cuántas horas y minutos son.
 
 
 
minutos = int(input("Ingresa un valor en minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")

# Ejercicio 14
#  Pide un número y determina si es un número positivo, negativo o cero.
  

numero = float(input("Ingresa un número: "))

if numero > 0:
    print("Es un número positivo")
elif numero < 0:
    print("Es un número negativo")
else:
    print("Es cero")

# Ejercicio 15
#  Ingresa la hora actual en formato de 24 horas. Si es de día (de 6 a 18), imprime "Es de día". Si es de noche (de 18 a 6),
#  imprime "Es de noche".
 
 
 
hora = int(input("Ingresa la hora actual (en formato 24 horas): "))

if 6 <= hora < 18:
    print("Es de día")
else:
    print("Es de noche")

 
# Ejercicio 16
#  Un usuario ingresa su edad y su altura. Si la edad es mayor de 18 y la altura mayor de 1.70 metros, imprime "Puedes
#  entrar a la montaña rusa". Si no, imprime "No puedes entrar".
  

 
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

if edad > 18 and altura > 1.70:
    print("Puedes entrar a la montaña rusa")
else:
    print("No puedes entrar")

 
 

# Ejercicio 17
# Pide al usuario que ingrese dos números. Si el primero es mayor que el segundo, imprime el primero. Si el segundo es
#  mayor que el primero, imprime el segundo. Si son iguales, imprime "Son iguales".

 
 
 
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

if numero1 > numero2:
    print(f"El primer número ({numero1}) es mayor.")
elif numero1 < numero2:
    print(f"El segundo número ({numero2}) es mayor.")
else:
    print("Son iguales.")
 
 
 
 

 
# Ejercicio 18
#  Solicita al usuario que ingrese un valor en segundos. Si los segundos son mayores a 3600, imprímelo como horas y
#  minutos. Si son menores o iguales a 3600, imprímelo como minutos y segundos.
  
 
 
 
 
 
 
 
 
# Ejercicio 19
#  Ingresa un número de 4 dígitos. Si el número es divisible entre 3, imprime "Divisible entre 3". Si no es divisible entre 3,
#  imprime "No divisible entre 3".
  

numero = int(input("Ingresa un número de 4 dígitos: "))

if numero % 3 == 0:
    print("Divisible entre 3")
else:
    print("No divisible entre 3")
 
# Ejercicio 20
#  Si el precio de un producto es mayor a 1000, aplica un descuento del 10%. Si es menor o igual a 1000, aplica un
#  descuento del 5%. Imprime el precio final después del descuento.
  
 
 
 
 
 
 
precio = float(input("Ingresa el precio del producto: "))

if precio > 1000:
    descuento = precio * 0.10
else:
    descuento = precio * 0.05

precio_final = precio - descuento
print(f"El precio final después del descuento es: {precio_final}")

 
 
 
 
 
 
 
 
# Ejercicio 21
#  Determina si un año es bisiesto. Un año es bisiesto si es divisible entre 4, pero no divisible entre 100, excepto si también
#  es divisible entre 400.



 
 
# Ejercicio 22
#  Pide un número e imprime si el número es menor que 0, igual a 0, mayor a 100 o mayor a 0 pero menor a 100
numero = int(input("Ingresa un número: "))

if numero < 0:
    print("El número es menor que 0.")
elif numero == 0:
    print("El número es igual a 0.")
elif numero > 100:
    print("El número es mayor a 100.")
else:
    print("El número es mayor a 0 pero menor a 100.")
