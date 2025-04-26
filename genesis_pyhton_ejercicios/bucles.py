# Contar del 1 al 10

i = 1
while i <= 10:
    print(i)
    i += 1
    
    
# Sumar números hasta que el usuario escriba 0

total = 0
num = int(input("Ingresa un número (0 para salir): "))
while num != 0:
    total += num
    num = int(input("Ingresa otro número (0 para salir): "))
print("Suma total:", total)



# Adivina el numero secreto
secreto = 7
adivina = int(input("Adivina el número (entre 1 y 10): "))

while adivina != secreto:
    print("Incorrecto, intenta de nuevo.")
    adivina = int(input("Adivina el número: "))

print("¡Correcto!")



#Intentos de contraseña
password = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    entrada = input("Introduce la contraseña: ")
    if entrada == password:
        print("Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta.")
        intentos += 1

if intentos == max_intentos:
    print("Acceso denegado. Demasiados intentos.")


#Hasta el numero 20
i = 2
while i <= 20:
    print(i)
    i += 2
