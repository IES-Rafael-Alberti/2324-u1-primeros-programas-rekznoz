def suma_de_enteros_hasta_n(n):
    suma = (n * (n + 1)) // 2
    return suma

if __name__ == "__main__":
    try:
        n = int(input("Ingrese un entero positivo n: "))
        if n < 1:
            raise ValueError("Debe ingresar un entero positivo.")
    except ValueError as e:
        print(f"Error: {e}")

    resultado = suma_de_enteros_hasta_n(n)
    print(f"La suma de los enteros desde 1 hasta {n} es: {resultado}")
