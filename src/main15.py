def calcular_ahorros_anuales(principal, tasa_interes, anos):
    for i in range(anos):
        principal += principal * tasa_interes
    return int(principal)

if __name__ == "__main__":
    try:
        principal = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))
        tasa_interes = 0.04  # Tasa de interés del 4%
        
        # Calcular los ahorros después de 1, 2 y 3 años
        ahorros_despues_1_anio = calcular_ahorros_anuales(principal, tasa_interes, 1)
        ahorros_despues_2_anios = calcular_ahorros_anuales(principal, tasa_interes, 2)
        ahorros_despues_3_anios = calcular_ahorros_anuales(principal, tasa_interes, 3)
        
        print(f"Ahorros después de 1 año: {round(ahorros_despues_1_anio, 2)}")
        print(f"Ahorros después de 2 años: {round(ahorros_despues_2_anios, 2)}")
        print(f"Ahorros después de 3 años: {round(ahorros_despues_3_anios, 2)}")
    except ValueError as e:
        print(f"Error: {e}")
