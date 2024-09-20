def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                raise ValueError("El número debe ser natural (mayor o igual a 0).")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")

def main():
    print("Calculadora de Máximo Común Divisor (MCD)")
    
    num1 = solicitar_numero("Ingrese el primer número natural: ")
    num2 = solicitar_numero("Ingrese el segundo número natural: ")
    
    mcd = calcular_mcd(num1, num2)
    print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")

if __name__ == "__main__":
    main()

