def suma_de_dos_numeros(a, b):
    suma = a + b
    return suma

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num1 += float(input("Ingrese el segundo número: "))
    num2 = float(input("Ingrese el tercer número: "))
    
    resultado = suma_de_dos_numeros(num1, num2)
    
    print(f"La suma de los tres números es: {resultado}")
