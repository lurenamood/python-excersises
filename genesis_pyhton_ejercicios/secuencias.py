# Ejercicios sobre Secuencias de Escape y F-strings en Python
#  Ejercicio 1: Saltos de línea
#  Usa el carácter de salto de línea \n para imprimir lo siguiente en múltiples líneas:
#  1. "Nombre: Ana"
#  2. "Edad: 25"
#  3. "Ciudad: Madrid"
#  Escribe el código usando un solo print.


print("Nombre: Ana\nEdad: 25\nCiudad: Madrid")

#  Ejercicio 2: Tabuladores
#  Usa el carácter de tabulador \t para formatear una lista de productos y precios, y que se vean alineados.- Producto    Precio- Manzana     1.50- Plátano     
# 1.20- Uva         2.00
#  Escribe el código para imprimirlo correctamente.
print("Producto\tPrecio")
print("Manzana\t1.50")
print("Plátano\t1.20")
print("Uva\t2.00")

#  Ejercicio 3: Barra invertida
#  Imprime una ruta de archivo utilizando barras invertidas. La ruta es: C:\Archivos\Trabajo\Proyectos.
print("C:\\Archivos\\Trabajo\\Proyectos")

#  Ejercicio 4: F-string con variables
#  Usa un f-string para imprimir las siguientes frases, donde las variables son:
#  1. Nombre: "Carlos"
#  2. Edad: 30
#  3. Ciudad: "Barcelona"
#  La salida debe ser:
#  Carlos tiene 30 años y vive en Barcelona.
nombre = "Carlos"
edad = 30
ciudad = "Barcelona"
print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

#  Ejercicio 5: Combinación de \n, \t, y \
#  Imprime lo siguiente usando secuencias de escape:
# C:\Users\Carlos
#  Nombre: Carlos Edad: 30 Dirección: Av. Central, 123
print("C:\\Users\\Carlos\nNombre: Carlos\nEdad: 30\nDirección: Av. Central, 123")


#  Ejercicio 6: F-string con cálculos
#  Usa un f-string para mostrar el resultado de la suma de dos números:- Número 1: 15- Número 2: 7
#  La salida debe ser:
#  El resultado de la suma de 15 y 7 es 22.
numero1 = 15
numero2 = 7
print(f"El resultado de la suma de {numero1} y {numero2} es {numero1 + numero2}.")

#  Ejercicio 7: F-string con formato numérico
#  Imprime el siguiente resultado con un f-string, donde la variable es un número flotante:- Precio: 3.4567
#  Imprime el precio con dos decimales. La salida debe ser:
#  El precio es 3.46
precio = 3.4567
print(f"El precio es {precio:.2f}")

#  Ejercicio 8: Uso de end y sep con print
#  Usa los parámetros end y sep para imprimir los siguientes números en una sola línea, separados por un 
# guion:- 5 10 15- 20 25 30
#  La salida debe ser:
#  5-10-15 20-25-30

print(5, 10, 15, sep='-', end=' ')
print(20, 25, 30, sep='-')
