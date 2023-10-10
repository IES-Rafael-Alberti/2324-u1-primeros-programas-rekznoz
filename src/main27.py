def calcular_costo_total(precio, unidades):
    costo_total = precio * unidades
    return costo_total

def mostrar_factura(nombre_producto, precio, unidades):
    costo_total = calcular_costo_total(precio, unidades)
    
    # Formatear las cadenas con el formato especificado
    nombre_formateado = nombre_producto
    precio_formateado = f"{precio:.2f}"
    unidades_formateado = f"{unidades:03d}"
    costo_total_formateado = f"{costo_total:.2f}"

    factura = f"{nombre_formateado} {precio_formateado} {unidades_formateado} {costo_total_formateado}"
    return factura

if __name__ == "__main__":
    try:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        unidades = int(input("Ingrese el número de unidades: "))

        factura = mostrar_factura(nombre_producto, precio, unidades)

        print("Factura:")
        print(factura)
    except ValueError as e:
        print(f"Error: {e}")
