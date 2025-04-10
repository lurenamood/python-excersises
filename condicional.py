
# # Ejercicios sobre Condicionales en Python

# # ## Ejercicio 1  
# # Pide al usuario su peso en kilogramos y su altura en metros. Calcula su índice de masa corporal (IMC) y clasifícalo en:
# # - **Bajo peso** (`IMC < 18.5`)
# # - **Peso normal** (`18.5 ≤ IMC < 24.9`)
# # - **Sobrepeso** (`25 ≤ IMC < 29.9`)
# # - **Obesidad** (`IMC ≥ 30`)

# # **Condición extra:** Si el peso es menor a 30 kg **o** mayor a 300 kg, imprime "Peso fuera de rango válido".  


# peso = float(print("Introduce tu peso: "))
# altura =  float(print("Introduce tu altura: "))
# imc = peso / (altura ** 2)

# if imc <= 18.5:
#     print("Tienes bajo peso")
# elif imc >= 18.5 and imc <= 24.9:
#     print("Peso normal")
# elif imc >= 25 and imc <= 29.9:
#     print("Sobrepeso")
# else:
#     print("Obesidad")








# # ## Ejercicio 2  
# # Solicita un número al usuario. Si es **múltiplo de 3 y de 5**, imprime "Múltiplo de 3 y 5".  
# # Si solo es múltiplo de 3, imprime "Múltiplo de 3".  
# # Si solo es múltiplo de 5, imprime "Múltiplo de 5".  
# # Si no es múltiplo de ninguno, imprime "No es múltiplo de 3 ni de 5".  


numero = int(input("Por favor, ingresa un número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Múltiplo de 3 y 5")
elif numero % 3 == 0:
    print("Múltiplo de 3")
elif numero % 5 == 0:
    print("Múltiplo de 5")
else:
    print("No es múltiplo de 3 ni de 5")









# # ## Ejercicio 3  
# # Pide al usuario tres números.  
# # - Si los **tres son iguales**, imprime "Todos son iguales".  
# # - Si **dos son iguales**, imprime "Dos números son iguales".  
# # - Si los tres son distintos, imprime "Todos son diferentes".  


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 == num2 == num3:
    print("Todos son iguales")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Dos números son iguales")
else:
    print("Todos son diferentes")











# # ## Ejercicio 4  
# # Solicita la velocidad de un vehículo en km/h.  
# # - Si la velocidad es mayor a `120 km/h`, imprime "Multa por exceso de velocidad".  
# # - Si está entre `80 y 120 km/h`, imprime "Velocidad moderada".  
# # - Si es menor a `80 km/h`, imprime "Velocidad baja".  
# # - **Extra:** Si la velocidad es negativa, imprime "Velocidad no válida" (usa `not`).  


velocidad = float(input("Ingresa la velocidad del vehículo en km/h: "))

if velocidad < 0:
    print("Velocidad no válida")
elif velocidad > 120:
    print("Multa por exceso de velocidad")
elif 80 <= velocidad <= 120:
    print("Velocidad moderada")
else:
    print("Velocidad baja")









# ## Ejercicio 5  
# Pide un número de **tres dígitos** e indica si es **capicúa** (se lee igual al revés).  
# **Condición extra:** Si el número no tiene tres dígitos, imprime "Número no válido".  


numero = input("Por favor, ingresa un número de tres dígitos: ")

if len(numero) == 3 and numero.isdigit():
    if numero == numero[::-1]: 
        print("El número es capicúa.")
    else:
        print("El número no es capicúa.")
else:
    print("Número no válido.")








# ## Ejercicio 6  
# Solicita un número y verifica si es primo.  
# Si el número es menor o igual a 1, imprime "No es un número primo" (usa `not`).  

numero = int(input("Por favor, ingresa un número: "))

if numero <= 1:
    print("No es un número primo")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):  # Verifica divisores hasta la raíz cuadrada del número
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es un número primo")
    else:
        print("No es un número primo")













# ## Ejercicio 7  
# Un cliente compra un producto.  
# - Si el total de la compra es mayor a `$1000` y es cliente frecuente, aplica **20% de descuento**.  
# - Si solo es cliente frecuente, aplica **10% de descuento**.  
# - Si el total es menor a `$1000`, aplica **5% de descuento**.  


total_compra = float(input("Ingresa el total de la compra: "))
cliente_frecuente = input("¿Eres cliente frecuente? (sí/no): ").strip().lower()

if total_compra > 1000 and cliente_frecuente == "sí":
    descuento = total_compra * 0.20
    print(f"Aplica un descuento del 20%. Total a pagar: ${total_compra - descuento:.2f}")
elif cliente_frecuente == "sí":
    descuento = total_compra * 0.10
    print(f"Aplica un descuento del 10%. Total a pagar: ${total_compra - descuento:.2f}")
else:
    descuento = total_compra * 0.05
    print(f"Aplica un descuento del 5%. Total a pagar: ${total_compra - descuento:.2f}")













# ## Ejercicio 8  
# Pide **tres números distintos** y determina cuál es el mayor y cuál es el menor.  

# **Condición extra:** Si **alguno de los números es negativo**, imprime "Los números deben ser positivos" y **no hagas comparaciones**.  


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 < 0 or num2 < 0 or num3 < 0:
    print("Los números deben ser positivos")
else:
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")















# ## Ejercicio 9  
# Solicita la calificación de un estudiante en una escala de `0 a 100`.  
# - **90 - 100:** "Excelente"  
# - **70 - 89:** "Bueno"  
# - **50 - 69:** "Regular"  
# - **Menor de 50:** "Reprobado"  
# - **Extra:** Si la calificación no está entre `0 y 100`, imprime "Calificación no válida" (usa `or`).  


calificacion = float(input("Ingresa la calificación del estudiante (0 a 100): "))

if calificacion < 0 or calificacion > 100:
    print("Calificación no válida")
elif calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Bueno")
elif calificacion >= 50:
    print("Regular")
else:
    print("Reprobado")











# ## Ejercicio 10  
# Pide un año al usuario y determina si es **bisiesto**.  
# Un año es bisiesto si es **divisible entre 4**, pero **no entre 100**, excepto si también es **divisible entre 400**.  


año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")












# ## Ejercicio 11  
# Solicita la edad del usuario y determina su grupo:
# - "Niño" si tiene **menos de 13 años**.  
# - "Adolescente" si tiene **entre 13 y 17 años**.  
# - "Adulto joven" si tiene **entre 18 y 30 años**.  
# - "Adulto" si tiene **entre 31 y 64 años**.  
# - "Adulto mayor" si tiene **65 o más**.  


edad = int(input("Ingresa tu edad: "))

if edad < 13:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 30:
    print("Adulto joven")
elif 31 <= edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")














# ## Ejercicio 12  
# Un empleado ingresa su **salario mensual** y los **años trabajados**.  
# - Si ha trabajado **más de 10 años y su salario es menor a 3000**, recibe un bono del **15%**.  
# - Si ha trabajado entre **5 y 10 años**, recibe un bono del **10%**.  
# - Si ha trabajado **menos de 5 años o su salario supera los 5000**, no recibe bono.  


salario = float(input("Ingresa tu salario mensual: "))
años_trabajados = int(input("Ingresa los años trabajados: "))

if años_trabajados > 10 and salario < 3000:
    bono = salario * 0.15
    print(f"Recibes un bono del 15%. Total bono: ${bono:.2f}")
elif 5 <= años_trabajados <= 10:
    bono = salario * 0.10
    print(f"Recibes un bono del 10%. Total bono: ${bono:.2f}")
else:
    print("No recibes bono.")













# ## Ejercicio 13  
# Pide **dos números** e indica si su **diferencia** es:  
# - "Mayor a 100"  
# - "Menor a 100"  
# - "Exactamente 100"  


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

diferencia = abs(num1 - num2)  # Calcula la diferencia absoluta

if diferencia > 100:
    print("Mayor a 100")
elif diferencia < 100:
    print("Menor a 100")
else:
    print("Exactamente 100")










# ## Ejercicio 14  
# Un usuario ingresa la **temperatura en grados Celsius**:  
# - **Menor a 0:** "Hace frío"  
# - **Entre 0 y 20:** "Clima templado"  
# - **Mayor a 20:** "Hace calor"  
# - **Extra:** Si la temperatura es mayor a `60` o menor a `-50`, imprime "Temperatura fuera de rango válido" (usa `or`).  

temperatura = float(input("Ingresa la temperatura en grados Celsius: "))

if temperatura > 60 or temperatura < -50:
    print("Temperatura fuera de rango válido")
elif temperatura < 0:
    print("Hace frío")
elif 0 <= temperatura <= 20:
    print("Clima templado")
else:
    print("Hace calor")











# ## Ejercicio 15  
# Solicita la hora en **formato 24 horas**:  
# - **6 - 12:** "Mañana"  
# - **12 - 18:** "Tarde"  
# - **18 - 24:** "Noche"  
# - **0 - 6:** "Madrugada"  
# - **Si la hora no está entre 0 y 24**, imprime "Hora no válida" (usa `not`).  


hora = float(input("Ingresa la hora en formato 24 horas: "))

if hora < 0 or hora >= 24:
    print("Hora no válida")
elif 6 <= hora < 12:
    print("Mañana")
elif 12 <= hora < 18:
    print("Tarde")
elif 18 <= hora < 24:
    print("Noche")
else:
    print("Madrugada")












# ## Ejercicio 16  
# Pide un número al usuario.  
# - Si **es positivo y mayor a 1000**, divídelo entre 5.  
# - Si **es positivo pero menor o igual a 1000**, multiplícalo por 3.  
# - Si **es negativo o igual a cero**, imprime "Debe ser mayor que 0".  

numero = float(input("Ingresa un número: "))

if numero > 1000:
    resultado = numero / 5
    print(f"El número es mayor a 1000. Resultado: {resultado:.2f}")
elif numero > 0:
    resultado = numero * 3
    print(f"El número es positivo y menor o igual a 1000. Resultado: {resultado:.2f}")
else:
    print("Debe ser mayor que 0")










# ## Ejercicio 17  
# Solicita **tres calificaciones** y calcula el promedio.  
# - **Si el promedio es mayor o igual a 9 y menor a 10**, imprime "Excelente".  
# - **Si está entre 7 y 8.9**, imprime "Bueno".  
# - **Si es menor a 7**, imprime "Reprobado".  
# - **Si alguna calificación está fuera del rango 0-10, imprime "Nota inválida"** (usa `or`).  

cal1 = float(input("Ingresa la primera calificación (0-10): "))
cal2 = float(input("Ingresa la segunda calificación (0-10): "))
cal3 = float(input("Ingresa la tercera calificación (0-10): "))

if cal1 < 0 or cal1 > 10 or cal2 < 0 or cal2 > 10 or cal3 < 0 or cal3 > 10:
    print("Nota inválida")
else:
    promedio = (cal1 + cal2 + cal3) / 3
    if promedio >= 9 and promedio < 10:
        print("Excelente")
    elif promedio >= 7 and promedio < 9:
        print("Bueno")
    else:
        print("Reprobado")


# ## Ejercicio 18  
# Un cliente compra **boletos para un evento**.  
# - **5 o más boletos:** Descuento **20%**.  
# - **3 o 4 boletos:** Descuento **10%**.  
# - **Menos de 3 boletos:** No hay descuento.  
# - **Si el usuario compra más de 10 boletos, imprime "Límite excedido"** (usa `not`).  










# ## Ejercicio 19  
# Pide al usuario que ingrese un **número de teléfono**.  
# - Si **tiene 10 dígitos**, imprime "Número válido".  
# - Si **tiene menos o más**, imprime "Número inválido".  








# ## Ejercicio 20  
# Un usuario ingresa su tipo de **suscripción** (`básica`, `estándar`, `premium`).  
# - **Básica:** "Acceso a contenido limitado".  
# - **Estándar:** "Acceso a contenido en HD".  
# - **Premium:** "Acceso a contenido en 4K y múltiples dispositivos".  
# - **Si ingresa un valor incorrecto, imprime "Suscripción inválida"** (usa `not`).