"Se omite el parámetro x en el llamado de la función ya que la variable es global"
def f():
    global x
    x = x + 1
    print("Valor de x dentro de f(x) = ", x)
    return x


# ALgoritmo principal
x = 3
print("Valor principal de x = ", x)
z = f(x)
print("Valor de x despues de llamar a f(x) = ", x)


"""
SALIDA:
Valor incial de x = 3
Valor de x dentro de f(x) = 4
Valor de x despues de llamar a f(x) = 3"""
