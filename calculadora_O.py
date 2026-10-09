while True:
    print("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")

    op = int(input("Opción: "))

    if op == 5:
        break

    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    if op == 1:
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print(a * b)
    elif op == 4:
        print(a / b)