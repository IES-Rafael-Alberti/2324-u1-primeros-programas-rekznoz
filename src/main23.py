def cambiar_dominio_correo(correo_actual, nuevo_dominio):
    partes = correo_actual.split('@')
    if len(partes) != 2:
        return None

    nombre_usuario, _ = partes
    nuevo_correo = f"{nombre_usuario}@{nuevo_dominio}"
    return nuevo_correo

if __name__ == "__main__":
    try:
        correo_actual = input("Ingrese su correo electrónico: ")
        nuevo_dominio = "ceu.es"

        nuevo_correo = cambiar_dominio_correo(correo_actual, nuevo_dominio)

        if nuevo_correo:
            print(f"Nuevo correo electrónico: {nuevo_correo}")
        else:
            print("El formato del correo electrónico no es válido.")
    except ValueError as e:
        print(f"Error: {e}")
