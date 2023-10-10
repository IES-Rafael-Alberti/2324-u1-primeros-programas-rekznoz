PRECIO_BARRA = 3.49  # Precio de una barra de pan en euros
DESCUENTO = 0.60    # Descuento del 60% para pan no fresco

def calcular_coste_final_barras_no_frescas(cantidad):
    coste_final = PRECIO_BARRA * cantidad * (1 - DESCUENTO)
    return round(coste_final,2)

if __name__ == "__main__":
    try:
        cantidad_barras = int(input("Ingrese el número de barras no frescas vendidas: "))
        
        if cantidad_barras < 0:
            raise ValueError("La cantidad de barras no puede ser negativa.")

        precio_barra = PRECIO_BARRA
        descuento = DESCUENTO
        coste_final = calcular_coste_final_barras_no_frescas(cantidad_barras)

        print(f"Precio habitual de una barra de pan: {precio_barra} €")
        print(f"Descuento por no ser fresca: {descuento * 100}%")
        print(f"Coste final total de barras no frescas: {coste_final:.2f} €")
    except ValueError as e:
        print(f"Error: {e}")
