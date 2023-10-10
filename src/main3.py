def calcular_expresiones(ancho, alto):
    resultado_1 = ancho / 2
    resultado_2 = ancho // 2
    resultado_3 = alto / 3
    resultado_4 = 1 + 2 * 5
    return resultado_1, resultado_2, resultado_3, resultado_4

if __name__ == "__main__":
    ancho = 17
    alto = 12.0

    resultado_1, resultado_2, resultado_3, resultado_4 = calcular_expresiones(ancho, alto)

    print("Resultado 1:", resultado_1)
    print("Resultado 2:", resultado_2)
    print("Resultado 3:", resultado_3)
    print("Resultado 4:", resultado_4)