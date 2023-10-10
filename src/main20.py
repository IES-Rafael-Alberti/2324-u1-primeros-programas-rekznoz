import re

def obtener_numero_telefono(numero):
    patron = r'\+34-(\d{9})-\d{2}'
    coincidencias = re.match(patron, numero)
    
    if coincidencias:
        numero_sin_prefijo_y_extension = coincidencias.group(1)
        return numero_sin_prefijo_y_extension
    else:
        return None

if __name__ == "__main__":
    try:
        numero_telefono = input("Ingrese un número de teléfono con el formato +34-XXXXXXXXX-XX: ")
        numero_sin_prefijo_y_extension = obtener_numero_telefono(numero_telefono)
        if numero_sin_prefijo_y_extension:
            print(f"Número de teléfono sin prefijo y extensión: {numero_sin_prefijo_y_extension}")
        else:
            print("El formato del número de teléfono no es válido.")
    except ValueError as e:
        print(f"Error: {e}")
