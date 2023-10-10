def division_entera(n, m):
    cociente = n // m
    resto = n % m
    return cociente, resto

if __name__ == "__main__":
    try:
        n = int(input("Por favor, ingrese un número entero n: "))
        m = int(input("Por favor, ingrese otro número entero m: "))

        if m == 0:
            raise ValueError("El divisor (m) no puede ser cero.")

        cociente, resto = division_entera(n, m)
        print(f"La división de {n} entre {m} da un cociente {cociente} y un resto {resto}")
    except ValueError as e:
        print(f"Error: {e}")
