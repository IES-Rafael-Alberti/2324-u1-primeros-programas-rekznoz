def calcular_peso_total_payasos_y_munecas(payasos, munecas):
    peso_payaso = 112  # Peso de cada payaso en gramos
    peso_muneca = 75   # Peso de cada muñeca en gramos
    peso_total = (payasos * peso_payaso) + (munecas * peso_muneca)
    return peso_total

if __name__ == "__main__":
    try:
        payasos = int(input("Ingrese el número de payasos vendidos: "))
        munecas = int(input("Ingrese el número de muñecas vendidas: "))

        peso_total = calcular_peso_total_payasos_y_munecas(payasos, munecas)
        print(f"El peso total del paquete a enviar es: {peso_total} gramos")
    except ValueError as e:
        print(f"Error: {e}")
