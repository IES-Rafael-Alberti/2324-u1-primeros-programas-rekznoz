
def bienvenida(nombre):
    return nombre

if __name__ == "__main__":
    nombre = input("Cual es tu nombre ")
    mensaje_bienvenida = bienvenida(nombre)
    print("Hola ",mensaje_bienvenida)