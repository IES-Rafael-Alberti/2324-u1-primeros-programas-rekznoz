def formatear_nombre(nombre_completo):
    nombre_minusculas = nombre_completo.lower()
    nombre_mayusculas = nombre_completo.upper()
    palabras = nombre_completo.split()
    nombre_capitalize = " ".join([palabra.capitalize() for palabra in palabras])
    
    return nombre_minusculas, nombre_mayusculas, nombre_capitalize

if __name__ == "__main__":
    try:
        nombre_completo = input("Ingrese su nombre completo: ")

        nombre_minusculas, nombre_mayusculas, nombre_capitalize = formatear_nombre(nombre_completo)

        print("Nombre en minúsculas:", nombre_minusculas)
        print("Nombre en mayúsculas:", nombre_mayusculas)
        print("Nombre capitalizado:", nombre_capitalize)
    except ValueError as e:
        print(f"Error: {e}")
