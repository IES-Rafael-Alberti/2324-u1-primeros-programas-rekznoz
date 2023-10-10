def obtener_fecha(dia, mes, anio):
    dia = dia.zfill(2)
    mes = mes.zfill(2)
    
    return dia, mes, anio

if __name__ == "__main__":
    try:
        fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
        
        partes = fecha_nacimiento.split("/")
        
        if len(partes) != 3:
            raise ValueError("El formato de la fecha debe ser dd/mm/aaaa.")
        
        dia, mes, anio = obtener_fecha(partes[0], partes[1], partes[2])

        print(f"Día: {dia}")
        print(f"Mes: {mes}")
        print(f"Año: {anio}")
    except ValueError as e:
        print(f"Error: {e}")
