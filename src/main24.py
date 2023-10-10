def obtener_euros_y_centimos(precio):
    euros = int(precio)
    centimos = int((precio - euros) * 100)
    return euros, centimos

if __name__ == "__main__":
    try:
        precio = float(input("Ingrese el precio del producto en euros (con dos decimales): "))
        
        euros, centimos = obtener_euros_y_centimos(precio)

        print(f"Número de euros: {euros}")
        print(f"Número de céntimos: {centimos}")
    except ValueError as e:
        print(f"Error: {e}")
