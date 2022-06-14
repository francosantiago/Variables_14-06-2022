def funcion(x):
    x.append(5)

# Programa principal 
x = [1, 2]
funcion(x)
print(x)

"""SALIDA:
[1, 2, 3]

El progrma principal gnera una lista de [1, 2] que se pasa a la función.
La función agrega el elemento 5 al final de la lista como la lista se pasa por referencia, automáticamente aparece con el programa principal en la llamada de la función.
Todos los arreglos , de cualquier tipo, y de cualquier dimensión, se pasan pro referencia"""