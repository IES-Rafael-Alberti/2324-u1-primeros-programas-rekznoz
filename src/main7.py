def suma_de_tres_numeros(a, b, c):
    suma = a + b + c
    return suma

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    resultado = suma_de_tres_numeros(num1, num2, num3)
    
    print(f"La suma de los tres números es: {resultado}")
