def calcular_iva_e_importe_sin_iva(importe_final):
    tipo_iva = 10  # Tipo de IVA del 10%
    iva_pagado = importe_final * tipo_iva / (100 + tipo_iva)
    importe_sin_iva = importe_final - iva_pagado
    return iva_pagado, importe_sin_iva

if __name__ == "__main__":
    importe_final = float(input("Ingrese el importe final del artículo: "))
    
    iva_pagado, importe_sin_iva = calcular_iva_e_importe_sin_iva(importe_final)
    
    print(f"IVA Pagado: {iva_pagado}")
    print(f"Importe sin IVA: {importe_sin_iva}")
