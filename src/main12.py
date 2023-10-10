def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return round(imc, 2)

if __name__ == "__main__":
    try:
        peso = float(input("Por favor, ingrese su peso en kilogramos: "))
        estatura = float(input("Por favor, ingrese su estatura en metros: "))

        if peso <= 0 or estatura <= 0:
            raise ValueError("El peso y la estatura deben ser valores positivos.")

        imc = calcular_imc(peso, estatura)
        print(f"Tu índice de masa corporal es: {imc}")
    except ValueError as e:
        print(f"Error: {e}")
