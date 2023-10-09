from main import main1 ,main2 ,main3 ,main4 ,main5 ,main6 ,main7 ,main8 ,main9, main10,main11,main12,main13,main14,main15,main16,main17,main18,main19,main20,main21,main22,main23,main24,main25,main26,main27

def test_bienvenida():
    assert main1.bienvenida("Rafa") == "Rafa"
    assert main1.bienvenida("Maria") == "Maria"
    assert main1.bienvenida("Adrian") == "Adrian"

def test_calcular_importe_total():
    assert main2.calcular_importe_total(10, 5) == 50
    assert main2.calcular_importe_total(8, 7.5) == 60
    assert main2.calcular_importe_total(0, 10) == 0

def test_calcular_expresiones():
    resultado_1, resultado_2, resultado_3, resultado_4 = main3.calcular_expresiones(17, 12.0)

    assert resultado_1 == 8.5
    assert resultado_2 == 8
    assert resultado_3 == 4.0
    assert resultado_4 == 11

def test_convertir_celsius_a_fahrenheit():
    assert main4.convertir_celsius_a_fahrenheit(0) == 32
    assert main4.convertir_celsius_a_fahrenheit(100) == 212
    assert main4.convertir_celsius_a_fahrenheit(-40) == -40

def test_calcular_precio_con_iva():
    assert main5.calcular_precio_con_iva(100, 10) == 110
    assert main5.calcular_precio_con_iva(50, 20) == 60
    assert main5.calcular_precio_con_iva(75, 5) == 78
    assert main5.calcular_precio_con_iva(0, 15) == 0

def test_calculadora_iva():
    iva, sin_iva = main6.calcular_iva_e_importe_sin_iva(110)
    assert iva == 10.0
    assert sin_iva == 100.0

def test_suma_de_tres_numeros():
    assert main7.suma_de_tres_numeros(1, 2, 3) == 6

def test_calculo_operacion_aritmetica():
    resultado = main10.calcular_operacion_aritmetica()
    assert resultado == 64.0

def test_suma_de_enteros_hasta_n():
    assert main11.suma_de_enteros_hasta_n(5) == 15
    assert main11.suma_de_enteros_hasta_n(10) == 55
    assert main11.suma_de_enteros_hasta_n(1) == 1
    assert main11.suma_de_enteros_hasta_n(100) == 5050

def test_calcular_imc():
    assert main12.calcular_imc(70, 1.75) == 22.86
    assert main12.calcular_imc(80, 1.80) == 24.69
    assert main12.calcular_imc(60, 1.60) == 23.44
    assert main12.calcular_imc(50, 1.70) == 17.30

def test_division_entera():
    cociente, resto = main13.division_entera(10, 3)
    assert cociente == 3
    assert resto == 1
    cociente, resto = main13.division_entera(20, 5)
    assert cociente == 4
    assert resto == 0
    cociente, resto = main13.division_entera(15, 7)
    assert cociente == 2
    assert resto == 1
    cociente, resto = main13.division_entera(-10, 3)
    assert cociente == -4
    assert resto == 2

def test_calcular_peso_total_payasos_y_munecas():
    peso_total = main14.calcular_peso_total_payasos_y_munecas(3, 5)
    assert peso_total == 711 
    peso_total = main14.calcular_peso_total_payasos_y_munecas(0, 10)
    assert peso_total == 750  
    peso_total = main14.calcular_peso_total_payasos_y_munecas(5, 0)
    assert peso_total == 560 
    peso_total = main14.calcular_peso_total_payasos_y_munecas(100, 200)
    assert peso_total == 26200

def test_calcular_ahorros_anuales():
    resultado = main15.calcular_ahorros_anuales(1000, 0.04, 1)
    assert resultado == 1040
    resultado = main15.calcular_ahorros_anuales(500, 0.04, 2)
    assert resultado == 540
    resultado = main15.calcular_ahorros_anuales(2000, 0.04, 3)
    assert resultado == 2249

def test_calcular_coste_final_barras_no_frescas():
    resultado = main16.calcular_coste_final_barras_no_frescas(5)
    assert resultado == 6.98
    resultado = main16.calcular_coste_final_barras_no_frescas(10)
    assert resultado == 13.96
    resultado = main16.calcular_coste_final_barras_no_frescas(0)
    assert resultado == 0.00  
    resultado = main16.calcular_coste_final_barras_no_frescas(100)
    assert resultado == 139.6

def test_generar_nombres():
    nombre = "Rafa"
    veces = 3
    resultado = main17.generar_nombres(nombre, veces)
    assert resultado == ["Rafa", "Rafa", "Rafa"]
    nombre = "Gustavo"
    veces = 5
    resultado = main17.generar_nombres(nombre, veces)
    assert resultado == ["Gustavo", "Gustavo", "Gustavo", "Gustavo", "Gustavo"]

def test_formatear_nombre():
    nombre_completo = "juan perez gonzalez"
    nombre_minusculas, nombre_mayusculas, nombre_capitalize = main18.formatear_nombre(nombre_completo)
    assert nombre_minusculas == "juan perez gonzalez"
    assert nombre_mayusculas == "JUAN PEREZ GONZALEZ"
    assert nombre_capitalize == "Juan Perez Gonzalez"
    nombre_completo = "MaRiA LoPeZ"
    nombre_minusculas, nombre_mayusculas, nombre_capitalize = main18.formatear_nombre(nombre_completo)
    assert nombre_minusculas == "maria lopez"
    assert nombre_mayusculas == "MARIA LOPEZ"
    assert nombre_capitalize == "Maria Lopez"

def test_contar_letras_nombre():
    nombre = "Juan"
    nombre_mayusculas, numero_letras = main19.contar_letras_nombre(nombre)
    assert nombre_mayusculas == "JUAN"
    assert numero_letras == 4
    nombre = "Ana"
    nombre_mayusculas, numero_letras = main19.contar_letras_nombre(nombre)
    assert nombre_mayusculas == "ANA"
    assert numero_letras == 3
    nombre = "Alberto"
    nombre_mayusculas, numero_letras = main19.contar_letras_nombre(nombre)
    assert nombre_mayusculas == "ALBERTO"
    assert numero_letras == 7
    nombre = ""
    nombre_mayusculas, numero_letras = main19.contar_letras_nombre(nombre)
    assert nombre_mayusculas == ""
    assert numero_letras == 0

def test_obtener_numero_telefono():
    numero = "+34-913724710-56"
    resultado = main20.obtener_numero_telefono(numero)
    assert resultado == "913724710"
    numero = "913724710-56"
    resultado = main20.obtener_numero_telefono(numero)
    assert resultado == None  
    numero = "+34-913724710"
    resultado = main20.obtener_numero_telefono(numero)
    assert resultado == None 
    numero = "913724710"
    resultado = main20.obtener_numero_telefono(numero)
    assert resultado == None 

def test_invertir_frase():
    frase = "Hola, mundo!"
    resultado = main21.invertir_frase(frase)
    assert resultado == "!odnum ,aloH"
    frase = ""
    resultado = main21.invertir_frase(frase)
    assert resultado == ""  # La frase invertida también es vacía
    frase = "Python cool"
    resultado = main21.invertir_frase(frase)
    assert resultado == "looc nohtyP"

def test_reemplazar_vocal_mayuscula():
    frase = "Hola, amigo!"
    vocal = "a"
    resultado = main22.reemplazar_vocal_mayuscula(frase, vocal)
    assert resultado == "HolA, Amigo!"
    frase = ""
    vocal = "e"
    resultado = main22.reemplazar_vocal_mayuscula(frase, vocal)
    assert resultado == ""
    frase = "Esta es una prueba"
    vocal = "x"
    resultado = main22.reemplazar_vocal_mayuscula(frase, vocal)
    assert resultado == frase

def test_cambiar_dominio_correo():
    correo_actual = "usuario@gmail.com"
    nuevo_dominio = "ceu.es"
    resultado = main23.cambiar_dominio_correo(correo_actual, nuevo_dominio)
    assert resultado == "usuario@ceu.es"
    correo_actual = "usuariogmail.com"
    nuevo_dominio = "ceu.es"
    resultado = main23.cambiar_dominio_correo(correo_actual, nuevo_dominio)
    assert resultado == None
    correo_actual = "usuario@gmail@com"
    nuevo_dominio = "ceu.es"
    resultado = main23.cambiar_dominio_correo(correo_actual, nuevo_dominio)
    assert resultado == None

def test_obtener_euros_y_centimos():
    precio = 10.75
    euros, centimos = main24.obtener_euros_y_centimos(precio)
    assert euros == 10
    assert centimos == 75
    precio = 5.00
    euros, centimos = main24.obtener_euros_y_centimos(precio)
    assert euros == 5
    assert centimos == 0
    precio = 3.99
    euros, centimos = main24.obtener_euros_y_centimos(precio)
    assert euros == 3
    assert centimos == 99
    precio = 0.50
    euros, centimos = main24.obtener_euros_y_centimos(precio)
    assert euros == 0
    assert centimos == 50

def test_obtener_fecha():
    dia, mes, anio = main25.obtener_fecha("5", "3", "2000")
    assert dia == "05"
    assert mes == "03"
    assert anio == "2000"
    dia, mes, anio = main25.obtener_fecha("10", "12", "1995")
    assert dia == "10"
    assert mes == "12"
    assert anio == "1995"
    dia, mes, anio = main25.obtener_fecha("1", "1", "2000")
    assert dia == "01"
    assert mes == "01"
    assert anio == "2000"
    dia, mes, anio = main25.obtener_fecha("9", "9", "99")
    assert dia == "09"
    assert mes == "09"
    assert anio == "99"
    dia, mes, anio = main25.obtener_fecha("8", "6", "200")
    assert dia == "08"
    assert mes == "06"
    assert anio == "200"

def test_separar_productos():
    entrada = "manzanas,peras,platanos"
    salida_esperada = ["manzanas", "peras", "platanos"]
    assert main26.separar_productos(entrada) == salida_esperada
    entrada = "leche,pan,huevos"
    salida_esperada = ["leche", "pan", "huevos"]
    assert main26.separar_productos(entrada) == salida_esperada

def test_mostrar_factura():
    nombre_producto = "Manzanas"
    precio = 2.5
    unidades = 10
    factura = main27.mostrar_factura(nombre_producto, precio, unidades)
    assert factura == "Manzanas 2.50 010 25.00"
    
    nombre_producto = "Leche"
    precio = 1.75
    unidades = 5
    factura = main27.mostrar_factura(nombre_producto, precio, unidades)
    assert factura == "Leche 1.75 005 8.75"

    nombre_producto = "Pan"
    precio = 0.99
    unidades = 20
    factura = main27.mostrar_factura(nombre_producto, precio, unidades)
    assert factura == "Pan 0.99 020 19.80"
