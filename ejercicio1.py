def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    while True:
        try:
            num1 = float(input("Ingrese el primer número natural: "))
            num2 = float(input("Ingrese el segundo número natural: "))
            
            # Convertir los números a enteros
            num1 = int(num1)
            num2 = int(num2)
            
            if num1 < 0 or num2 < 0:
                raise ValueError("Los números deben ser naturales (mayores o iguales a 0).")
            
            mcd = calcular_mcd(num1, num2)
            print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")
            break  # Salir del bucle si la entrada es válida
            
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")

main()


