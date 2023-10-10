def invertir_frase(frase):
    frase_invertida = frase[::-1]
    return frase_invertida

if __name__ == "__main__":
    try:
        frase = input("Introduzca una frase: ")
        
        frase_invertida = invertir_frase(frase)

        print("Frase invertida:", frase_invertida)
    except ValueError as e:
        print(f"Error: {e}")
