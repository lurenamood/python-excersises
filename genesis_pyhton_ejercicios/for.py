# 📝 Ejercicios con for en Python

#FACTORIAL(x)


 #1
for n in range(1, 6):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}")
    
    
#2
numeros = [5, 4, 3, 2, 1]
for n in numeros:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}")
    
    
#3
import math
print(math.factorial(5))



#4
num = int(input("Ingr el numero: "))
facto = 1
for i in range(num, 0, -1):
    print(f"EL numero que se imprime {i}")
    facto *= i 
print("Factorial de ", num, "is ", facto) 


# Imprimir números del 1 al 20
# # Muestra en pantalla los números del 1 al 20, uno por línea.
for i in range(1, 21):
    print(i)




# Sumar los primeros 100 números
# Usa un bucle for para sumar todos los números del 1 al 100 e imprime el resultado.

suma = 0
for i in range(1, 101):
    suma += i
print(f"La suma de los primeros 100 números es: {suma}")




# Tabla de multiplicar
# Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.


numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



# Números pares del 1 al 50
# Imprime solo los números pares del 1 al 50.


for i in range(2, 51, 2):  # Inicia desde 2 y da saltos de 2
    print(i)



# Contar letras 'a' en una palabra
#Pide al usuario una palabra y cuenta cuántas veces aparece la letra 'a'.


palabra = input("Ingresa una palabra: ")
contador = 0
for letra in palabra:
    if letra.lower() == 'a':
        contador += 1
print(f"La letra 'a' aparece {contador} veces en la palabra.")







# Imprimir una lista al revés
# Dada una lista de números, imprímela en orden inverso usando for.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
for numero in reversed(numeros):
    print(numero)





# Factorial de un número
# Pide al usuario un número entero positivo y calcula su factorial con un for.


numero = int(input("Ingresa un número entero positivo: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")



# Contar vocales en una frase
# Pide una frase y cuenta cuántas vocales (a, e, i, o, u) tiene.

frase = input("Ingresa una frase: ")
vocales = "aeiou"
contador_vocales = 0
for letra in frase.lower():
    if letra in vocales:
        contador_vocales += 1
print(f"La frase tiene {contador_vocales} vocales.")





# Crear una pirámide de asteriscos
# Usa un bucle for para imprimir una pirámide así:
altura = 5  
for i in range(1, altura + 1):
    print("*" * i)










# Número más grande de una lista
# Dada una lista de números, encuentra el número más grande sin usar max().




numeros = [5, 12, 18, 7, 34, 9, 21]  # Puedes cambiar esta lista por la que quieras
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f"El número más grande de la lista es: {maximo}")
