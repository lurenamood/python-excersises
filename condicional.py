
# Ejercicios sobre Condicionales en Python

# ## Ejercicio 1  
# Pide al usuario su peso en kilogramos y su altura en metros. Calcula su índice de masa corporal (IMC) y clasifícalo en:
# - **Bajo peso** (`IMC < 18.5`)
# - **Peso normal** (`18.5 ≤ IMC < 24.9`)
# - **Sobrepeso** (`25 ≤ IMC < 29.9`)
# - **Obesidad** (`IMC ≥ 30`)

# **Condición extra:** Si el peso es menor a 30 kg **o** mayor a 300 kg, imprime "Peso fuera de rango válido".  


peso = float(print("Introduce tu peso: "))
altura =  float(print("Introduce tu altura: "))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Tienes bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")








# ## Ejercicio 2  
# Solicita un número al usuario. Si es **múltiplo de 3 y de 5**, imprime "Múltiplo de 3 y 5".  
# Si solo es múltiplo de 3, imprime "Múltiplo de 3".  
# Si solo es múltiplo de 5, imprime "Múltiplo de 5".  
# Si no es múltiplo de ninguno, imprime "No es múltiplo de 3 ni de 5".  











# ## Ejercicio 3  
# Pide al usuario tres números.  
# - Si los **tres son iguales**, imprime "Todos son iguales".  
# - Si **dos son iguales**, imprime "Dos números son iguales".  
# - Si los tres son distintos, imprime "Todos son diferentes".  













# ## Ejercicio 4  
# Solicita la velocidad de un vehículo en km/h.  
# - Si la velocidad es mayor a `120 km/h`, imprime "Multa por exceso de velocidad".  
# - Si está entre `80 y 120 km/h`, imprime "Velocidad moderada".  
# - Si es menor a `80 km/h`, imprime "Velocidad baja".  
# - **Extra:** Si la velocidad es negativa, imprime "Velocidad no válida" (usa `not`).  











# ## Ejercicio 5  
# Pide un número de **tres dígitos** e indica si es **capicúa** (se lee igual al revés).  
# **Condición extra:** Si el número no tiene tres dígitos, imprime "Número no válido".  










# ## Ejercicio 6  
# Solicita un número y verifica si es primo.  
# Si el número es menor o igual a 1, imprime "No es un número primo" (usa `not`).  














# ## Ejercicio 7  
# Un cliente compra un producto.  
# - Si el total de la compra es mayor a `$1000` y es cliente frecuente, aplica **20% de descuento**.  
# - Si solo es cliente frecuente, aplica **10% de descuento**.  
# - Si el total es menor a `$1000`, aplica **5% de descuento**.  















# ## Ejercicio 8  
# Pide **tres números distintos** y determina cuál es el mayor y cuál es el menor.  

# **Condición extra:** Si **alguno de los números es negativo**, imprime "Los números deben ser positivos" y **no hagas comparaciones**.  

















# ## Ejercicio 9  
# Solicita la calificación de un estudiante en una escala de `0 a 100`.  
# - **90 - 100:** "Excelente"  
# - **70 - 89:** "Bueno"  
# - **50 - 69:** "Regular"  
# - **Menor de 50:** "Reprobado"  
# - **Extra:** Si la calificación no está entre `0 y 100`, imprime "Calificación no válida" (usa `or`).  













# ## Ejercicio 10  
# Pide un año al usuario y determina si es **bisiesto**.  
# Un año es bisiesto si es **divisible entre 4**, pero **no entre 100**, excepto si también es **divisible entre 400**.  














# ## Ejercicio 11  
# Solicita la edad del usuario y determina su grupo:
# - "Niño" si tiene **menos de 13 años**.  
# - "Adolescente" si tiene **entre 13 y 17 años**.  
# - "Adulto joven" si tiene **entre 18 y 30 años**.  
# - "Adulto" si tiene **entre 31 y 64 años**.  
# - "Adulto mayor" si tiene **65 o más**.  
















# ## Ejercicio 12  
# Un empleado ingresa su **salario mensual** y los **años trabajados**.  
# - Si ha trabajado **más de 10 años y su salario es menor a 3000**, recibe un bono del **15%**.  
# - Si ha trabajado entre **5 y 10 años**, recibe un bono del **10%**.  
# - Si ha trabajado **menos de 5 años o su salario supera los 5000**, no recibe bono.  















# ## Ejercicio 13  
# Pide **dos números** e indica si su **diferencia** es:  
# - "Mayor a 100"  
# - "Menor a 100"  
# - "Exactamente 100"  












# ## Ejercicio 14  
# Un usuario ingresa la **temperatura en grados Celsius**:  
# - **Menor a 0:** "Hace frío"  
# - **Entre 0 y 20:** "Clima templado"  
# - **Mayor a 20:** "Hace calor"  
# - **Extra:** Si la temperatura es mayor a `60` o menor a `-50`, imprime "Temperatura fuera de rango válido" (usa `or`).  












# ## Ejercicio 15  
# Solicita la hora en **formato 24 horas**:  
# - **6 - 12:** "Mañana"  
# - **12 - 18:** "Tarde"  
# - **18 - 24:** "Noche"  
# - **0 - 6:** "Madrugada"  
# - **Si la hora no está entre 0 y 24**, imprime "Hora no válida" (usa `not`).  














# ## Ejercicio 16  
# Pide un número al usuario.  
# - Si **es positivo y mayor a 1000**, divídelo entre 5.  
# - Si **es positivo pero menor o igual a 1000**, multiplícalo por 3.  
# - Si **es negativo o igual a cero**, imprime "Debe ser mayor que 0".  











# ## Ejercicio 17  
# Solicita **tres calificaciones** y calcula el promedio.  
# - **Si el promedio es mayor o igual a 9 y menor a 10**, imprime "Excelente".  
# - **Si está entre 7 y 8.9**, imprime "Bueno".  
# - **Si es menor a 7**, imprime "Reprobado".  
# - **Si alguna calificación está fuera del rango 0-10, imprime "Nota inválida"** (usa `or`).  








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