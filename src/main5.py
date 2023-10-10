def calcular_precio_con_iva(importe_sin_iva, tipo_iva):
    precio_con_iva = importe_sin_iva * (1 + tipo_iva / 100)
    return int(precio_con_iva)

if __name__ == "__main__":
    importe_sin_iva = float(input("Ingrese el importe sin IVA del artículo: "))
    tipo_iva = float(input("Ingrese el tipo de IVA a aplicar (porcentaje): "))
    
    precio_final = calcular_precio_con_iva(importe_sin_iva, tipo_iva)
    
    print(f"El precio final del artículo con {tipo_iva}% de IVA es: {precio_final}")
