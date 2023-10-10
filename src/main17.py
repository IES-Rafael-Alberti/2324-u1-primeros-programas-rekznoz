
def generar_nombres(nombre, veces):
    nombres = [nombre] * veces
    return nombres

def main():
    nombre = input("Ingrese su nombre: ")
    try:
        veces = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return

    resultado = generar_nombres(nombre, veces)
    for nombre in resultado:
        print(nombre)
