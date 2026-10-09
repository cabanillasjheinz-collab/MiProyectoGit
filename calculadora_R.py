import math

while True:
    print("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia\n6. Raíz cuadrada\n7. Salir")
    
    op = int(input("Opción: "))
    
    if op == 7:
        break
        
    # Si elige opciones del 1 al 5, pide dos números
    if op >= 1 and op <= 5:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        
        if op == 1: print(a + b)
        elif op == 2: print(a - b)
        elif op == 3: print(a * b)
        elif op == 4: print(a / b)
        elif op == 5: print(a ** b)
        
    # Si elige raíz cuadrada (opción 6), solo pide un número
    elif op == 6:
        a = float(input("Número: "))
        print(math.sqrt(a))