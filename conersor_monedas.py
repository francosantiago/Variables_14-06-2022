print("---------------------------------------")
print("-------- CONVERSOR DE MONEDAS ---------")
print("---------------------------------------")

# función para hacer la converción
def convertir(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")


# Función principal del programa
def funcion_principal():
    menu = """"
    Bienvenidos al conversor de moneda
    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos
    
    Elije la opción:   """

    opcion= int(input(menu))
    if opcion == 1:
        convertir("colombianos", 3966)
    elif opcion == 2:
        convertir("Argentinos", 122.52)
    elif opcion == 3:
        convertir("Mexicanos", 20.62)
    else:
        print("Ingrese una opción correcta")

# Inicializar el programa
if __name__ == "__main__":
    funcion_principal()
