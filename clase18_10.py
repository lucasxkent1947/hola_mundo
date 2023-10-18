""" Condicionar permitir dividir el flujo de un programa en diferentes caminos """

##IF 

""" if True:
    print("Se cumple la condicion")

 """
""" a = 5
if a == 2:
    print("A vale 2")
if a == 5:
    print("A vale 5")
    
 """
 
""" a = 5
b = 10
if a == 5:
    print("A vale", a)
    if b == 10:
        print("y b vale", b)
        
         """

""" a = 5
b = 10

if a == 5 and b == 10:
    print("A es igual a 5 y B es igual a 10") """
    
# ELSE

""" n = 11
if n == 10:
    print(n, "es igual a 10")
else:
    print(n, "es igual a otro numero distinto a 10")


 """

#ELIF (sino si)

""" comando = "Salir"

if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "Saludar":
    print("Hola, espero que te lo estes pasando bien aprendiendo")
elif comando == "Salir":
    print("Saliendo del sistema")
else:
    print("Este comando no se reconoce")
     """



""" nota = float(input("Introduce una nota: "))

if nota >= 9:
    print("La rompiste")
elif nota >= 7 and nota < 9:
    print("Buen trabajo")
elif nota >= 6 and nota < 7:
    print("Esta bien...")
elif nota >= 5 and nota <6 :
    print("Suficiente")
else:
    print("Desaprobaste") """

    
    
#                                   ITERACIONES
#Iterar significa realizar una accion varias veces. Cada vez que esto se repite se denomina ITERACION.

# WHILE


""" c = 0

while c <=5 :
    c+=1
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale", c) """
    
    
# Break = Romper

""" c=0
while c<=5:
    c+=1
    if (c==2):
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale: ", c)
     """
 
 
#CONTINUE = saltar     
""" c = 0
while c<=5:
    c+=1
    if c==3 or c==4:
        continue
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale", c)
    
 """
 
 
""" 
print("Bienvenido al menú interactivo")
while(True):
    print("Que queres hacer? Escribi una opcion
          1) Saludar
          2) Sumar dos numeros
          3) Salir
          ")
    opcion = input("Escribilo")
    if opcion == "1":
        print("Hola, te estamos saludando")
    elif opcion == "2":
        n1 = float(input("Introduce un numero a sumar"))
        n2 = float(input("Introduce otro numero a sumar"))
        print("El resultado de la suma de tus nros es:", n1+n2)
    elif opcion == "3":
        print("Chau")
        break
    else:
        print("No se que me quisiste decir")
         """


# FOR 

""" numeros = [1,2,3,4,5,6,7,8,9,10]
" indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1 "

for numero in numeros:
    numero *= 10
    print(numero) """
    
    
""" indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *=10 
    indice+=1
print(numeros) """

""" numeros = [1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate(numeros):
    numeros[indice] *=10
print(numeros)
 """
""" 
cadena = "Hola Chicxs Unahur"
for caracter in cadena:
    print(caracter)
 """
""" 
cadena = "Hola Chicxs Unahur"
cadena2= ""
for caracter in cadena:
    cadena2 += caracter*3
print(cadena2) """

""" for item in range(10):
    print(item) """
    
    
    