def contar_letras_nombre(nombre):
    nombre_mayusculas = nombre.upper()
    numero_letras = len(nombre)
    return nombre_mayusculas, numero_letras

if __name__ == "__main__":
    try:
        nombre = input("Ingrese su nombre: ")
        
        nombre_mayusculas, numero_letras = contar_letras_nombre(nombre)

        print(f"{nombre_mayusculas} tiene {numero_letras} letras.")
    except ValueError as e:
        print(f"Error: {e}")
