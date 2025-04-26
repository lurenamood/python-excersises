#1

personas = []

while True:
    print("\n1. Agregar")
    print("2. Ver")
    print("3. Eliminar")
    print("4. Salir")

    opcion = input("Opción: ")

    match opcion:
        case "1":
            nombre = input("Nombre: ")
            personas.append(nombre)

        case "2":
            for i in range(len(personas)):
                print(f"{i + 1}. {personas[i]}")

        case "3":
            for i in range(len(personas)):
                print(f"{i + 1}. {personas[i]}")
            indice = int(input("Número a eliminar: ")) - 1
            if 0 <= indice < len(personas):
                personas.pop(indice)

        case "4":
            break

        case _:
            print("Opción no válida.")


#2
elementos = []

while True:
    print("\nMENÚ:")
    print("1. AGREGAR")
    print("2. VER")
    print("3. BORRAR")
    print("4. SALIR")
    
    # opcion = input("Qué quieres Hacer?")
    
    # if
    
    match input("Seleccione (1-4): "):
        case "1":
            nuevo = input("Ingrese el elemento: ")
            elementos.append(nuevo)
            print(f"'{nuevo}' añadido")

        case "2":
            if not elementos:
                print("La lista está vacía")
            else:
                print("\nELEMENTOS:")
                for i, item in enumerate(elementos, 1):
                    print(f"{i}. {item}")

        case "3":
            if not elementos:
                print("No hay elementos para quitar")
            else:
                print("\nElementos disponibles:")
                for i, item in enumerate(elementos, 1):
                    print(f"{i}. {item}")
                try:
                    num = int(input("Número a quitar: "))
                    if 1 <= num <= len(elementos):
                        eliminado = elementos.pop(num-1)
                        print(f"'{eliminado}' eliminado")
                    else:
                        print("Número fuera de rango")
                except ValueError:
                    print("Debe ingresar un número")

        case "4":
            print("Programa terminado")
            break

        case _:
            print("Opción no válida")
