def suma_de_tres_numeros(a, b, c):
    suma = a + b + c
    return suma

if __name__ == "__main__":
    resultado = suma_de_tres_numeros(float(input("Ingrese el primer número: ")), float(input("Ingrese el segundo número: ")), float(input("Ingrese el tercer número: ")))
    print(f"La suma de los tres números es: {resultado}")
