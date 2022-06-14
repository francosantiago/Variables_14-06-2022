# FUNCIONES

## VARIABLES LOCALES Y GLOBALES

### VARIABLES LOCALES
- Variables que se definen dentro de una función.
- Son validas únicamente dentro de la función.
- Las variables correspondientes a las función solamente son las accesibles por la función, es decir, al usarlas fuera de la función marcará error.
- Una variable del algoritmo principal que se pasa a una función donde se modifíca y es variable local, cambia su valor en la función, pero NO tiene el algoritmo principal.

### VARIABLES GLOBALES
- Son aquellas que no importa donde se usen o modifiquen, siempre conservan los valores asignados, ya sea en el algoritmo principal o en las funciones.
- Para hace rque una función sea global, hay que definirla como tal por medio de la instrucción `global nombre_variable`.

## LLAMADO POR VALOR Y LLAMADO POR REFERENCIA

### Paso por valor
- Cuando se pasa una variable a una función creando una nueva localidad de memoria, donde se copian los valores de los parametros de la función.
- La memoria ocupada aumenta de tamaño.
- Aunque en python no se aumenta la memoria, el paso de la variable es quivalente a paso por valor.

### Paso por referencia
- La variable se puede modificar en la función y el cambio siempre se realiza usando la referencia a la localidad de memoria donde se almacena la variable. Ej: Variables tipo lista.

## FUNCIONES LAMBDA
- Declaración de una función en un solo renglon
`f = lambda parámetros: expresión de la función f`
