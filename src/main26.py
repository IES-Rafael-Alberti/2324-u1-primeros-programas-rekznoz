def separar_productos(entrada):
    return entrada.split(',')

if __name__ == "__main__":
    productos = input("Ingrese los productos de la cesta de la compra separados por comas: ")
    lista_productos = separar_productos(productos)
    
    for producto in lista_productos:
        print(producto.strip())
