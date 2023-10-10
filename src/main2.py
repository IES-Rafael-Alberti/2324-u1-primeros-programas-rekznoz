
def calcular_importe_total(horas_trabajo, precio_hora):
    return horas_trabajo * precio_hora

if __name__ == "__main__":
    horas_trabajo = int(input("Horas de trabajo "))
    precio_hora = float(input("Precio por hora "))

    importe_total = calcular_importe_total(horas_trabajo, precio_hora)
    print("Importe total", importe_total)