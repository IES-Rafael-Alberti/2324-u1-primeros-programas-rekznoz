def reemplazar_vocal_mayuscula(frase, vocal):
    vocal_mayuscula = vocal.upper()
    frase_modificada = frase.replace(vocal, vocal_mayuscula)
    return frase_modificada

if __name__ == "__main__":
    try:
        frase = input("Introduzca una frase: ")
        vocal = input("Introduzca una vocal: ")

        if len(vocal) != 1 or vocal.lower() not in "aeiou":
            raise ValueError("Por favor, introduzca una única vocal válida (a, e, i, o, u).")

        frase_modificada = reemplazar_vocal_mayuscula(frase, vocal)

        print("Frase modificada:", frase_modificada)
    except ValueError as e:
        print(f"Error: {e}")
