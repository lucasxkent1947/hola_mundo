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



impares = sum(range(0,101,2))
print(impares)


