""" examen1 = float(input("Hola, ingresá tu primer nota:"))
examen2 = float(input("Hola, ingresá tu segunda nota:"))
examen3 = float(input("Hola, ingresá tu segunda nota:"))


print( examen1*0.15 + examen2*0.35 + examen3*0.5) """



""" matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)

 """


""" CONSIGNA:
    -Escribi un programa que lea mediante input y nos permita seleccionar 4 opciones en un menu:
        
        1- Mostrar una suma de los numeros
        2- Mostrar una resta de dos numeros
        3- Mostrar una multiplicacion de dos nros
        4- Si selecciona esto, se interrumpe el programa.
        5- Si no hay opciones validad, que indique que esta todo mal.
         """
         
""" nro1 = float(input("ingresa el primer nro: "))
nro2 = float(input("ingresa el segundo nro: "))

while True:
    print("Hola. Queres sumar, restar o multiplicar? o salir")
    opcion = (input("Escribi tu eleccion: "))
    
    if opcion == "sumar":
        print("Su suma es: ", nro1 + nro2)
    elif opcion == "restar":
        print("Su resta es: ", nro1 - nro2)
    elif opcion == "multiplicar":
        print("Su multiplicacion es: ", nro1 * nro2)
    elif opcion == "salir":
        break
    else:
        print("Opcion incorrecta") """
        
        
"""     Escribi un programa que lea un nro impar por teclado. si se introduce un numero que no es impar, se repite hasta que lo haga bien """

""" numero = 0
while numero % 2 == 0:
    numero = int(input("Ingresa un nro impar: "))
if numero % 1 == 0:
    print("Bien pusiste un nro impar") """
    
    
""" Escribi un codigo que sume todos los numeros enteros impares desde el 0 hasta el 100: """



""" impares = sum(range(0,101,2))
print(impares)
 """



""" suma = 0
numeros = int(input("Ingresa la cantidad de estudiantes: "))
for x in range(numeros):
    suma += float(input("Ingresa la calificacion del estudiante: "))
print(" Nota promedio del curso: ", suma/numeros) """


"""" Escribí un programa que pida al usuario un nro entero 0 al 9, y que mientras el nro no sea correcto se repita el proceso. Luego se debe comprobar si el nro se encuentra en la lista y notificarlo"""


""" numeros = [1,2,3,4,5,6,7,8,9]
while True:
    nro = int(input("Elegí el nro de tu camiseta: "))
    if nro > 9 or nro < 0:
        print("No existe ese nro de camiseta")
        continue
    if nro in numeros:
        break
    print("Sorry, la camiseta ", nro, "ya fue elegida")
print("Perfecto, seleccionaste la camiseta ", nro )
 """

""" Utilizando la funcion range() y la conversion a listas genera las siguientes listas dinamicamente: 

Todos los nros del 0 al 10
Todos los nros del -10 al 0
Todos los pares del 0 al 20
Todos los impares entre -20 y 0
Todos los nros multiples de 0 al 50

"""

""" print(list(range(11)))
print(list(range(-10,1)))
print(list(range(0,21, 2)))
print(list(range(-19,0,2)))
print(list(range(0,51, 5))) """


""" Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningun elemento en la nueva lista """

""" lista_1 = ["U", "N", "I", "V", "E", "R", "S", "I", "D", "A", "D", " ", "H", "U", "R", "L", "I", "N", "G", "H", "A", "M"]
lista_2 = ["D", "E", "P", "O","R", "T", "I", "V", "O", " ", "M", "O", "R", "O","N"]
lista_3 = []


for item in lista_1:
    if item in lista_2 and item not in lista_3:
        lista_3.append(item)
        
print("Lista 3: ", lista_3)

 """

#Año Bisiesto
""" anio = int(input("Ingresa un año: "))

if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("ingresaste un año bisiesto")
else:
    print("el año no es bisiesto") """
    
""" def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado

# area_rectangulo(15,10)

print(area_rectangulo(15,10))
 """


""" pi = 3.14159
def area_circulo(radio):
    resultado = (radio**2) * pi
    return resultado
print(area_circulo(5))
 """
""" 
def relacion(nro1, nro2):
    if nro1 > nro2:
        return 1
    elif nro1 < nro2:
        return -1
    else:
        return 0
    
print(relacion(20, 10)) """



""" lista = [1,9,75,5,3,2,10,4,32,8]
def separar(lista):
    lista_pares = []
    lista_impares = []
    for i in lista:
        if i%2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    lista_pares.sort()
    lista_impares.sort()
    return lista_pares, lista_impares


lista_pares, lista_impares  = separar([1,9,75,5,3,2,10,4,32,8])

print(lista_impares)
print(lista_pares)
     """