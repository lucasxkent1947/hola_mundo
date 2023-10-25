""" def saludar():
    print("Hola, muchachxs como estan?")
    
saludar() """

#SCOPE

""" def test():
    n=10
test()
 """

""" n = 1000
def test():
    print(n)
    
test() """


""" def test():
    print(n)

test() """


""" def test():
    o=10    #Esta variable solo va a existir dentro de la funcion
    print(o)
 
o = 100 # Esta otra variable externa, no será modificada
test()
print(o)
 """
 
# Transformamos global el alcance de lo definido dentro de la función 
""" def test():
    global o
    o = 5
    print(o)
    
o = 50
test()
print(o)

 """
 
""" def test ():
    return "Una cadena"
test() """

""" def test():
    return [123,456,7890]

print(test())
print(test()[-1])
print(test()[1:4])



lista = test()
print(lista[-1]) """



""" def test():
    return "Una cadena", 1000, [4,5,6]
print(test())


cadena, numero, lista = test()

print(cadena)
print(numero)
print(lista) """


""" def nombre():
    saludo = print("Hola! Como va? ")
    return saludo
    print("Hola")
nombre() """


""" def suma(a,b):   #Los valores que se reciben
    return a+b

resultado = suma(10,50)  #Estos son los valores que se envian
print(resultado)

 """
 
""" def resta(x,y):
    return x-y

print(resta())

 """
 
"""  
def duplicar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *=2
        
x = [10,20,30]
duplicar_valores(x)

print(x)
 """

def duplicar_valor(numero):
    return numero * 2
n = 100
n = duplicar_valor(n)
print(n)