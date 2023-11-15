""" class Product:
    def __init__(self, referencia, tipo, nombre, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
        
adorno = Product('000A', 'adorno', 'vaso adornado', 'vaso de vidrio')

print(adorno)
print(adorno.tipo)
 """


""" class Product:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
                f"DESCRIPCION\t\t {self.descripcion}\n"
               

class Adorno(Product):
    pass

adorno = Adorno (1, "Vaso Adorno", 30, "Vaso En Oferta")

print(adorno)


class Alimentos(Product):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
                f"DESCRIPCION\t\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
                f"DISTRIBUIDOR\t\t {self.distribuidor} \n"
                
class Libritos(Product):
    isbn= ""
    autor = ""
    
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCION\t\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"
               
               
               
alimento = Alimentos(15235, "Levadura", 8, "300ml")
alimento.productor = "Calsa"
alimento.distribuidor = "Distribuidora S.A"
print(alimento)



libro = Libritos(3000, "El Principito", 1000, "Un cuentito")
libro.isbn = "1-32153156165-5"
libro.autor = "Un Frances"

print(libro)




productos = [adorno, alimento]
productos.append(libro)

print(productos)


for producto in productos:
    print(producto)
    
    
for producto in productos:
    print(producto.referencia, producto.nombre)
    
    
"""# for producto in productos:
    #print(producto.autor) """
    

""" for producto in productos:
    if(isinstance(producto, Adorno)):
        print(producto.referencia, producto.nombre)
    elif(isinstance(producto, Alimentos)):
        print(producto.referencia, producto.nombre, producto.productor)
    elif(isinstance(producto, Libritos)):
        print(producto.referencia, producto.nombre, producto.isbn)
        
        
        
def aplicardescuento(producto, descuento):
    producto.pvp = producto.pvp - (producto.pvp/100 * descuento)
    

print(alimento)
aplicardescuento(alimento, 50)
print(alimento)
 """




""" class Test:
    pass


test10 = Test()
test20 = test10

test10.algo = "Prueba"

print(test20 == test10)


try:
    print(test20.algo)
except Exception as x:
    print(x)



from copy import copy
class Test:
    pass

test10 = Test()
test20 = copy(test10)

test10.algo= "Prueba"

print(test10== test20)


try:
    print(test20.algo)
except Exception as x:
    print(x)
    
   
    
from copy import copy

lista = [1,2,3,4,5]
lista2 = copy(lista)
lista = None


print(lista)
print(lista2)
 """




## HERENCIA MULTIPLE

""" class A:
    def __init__(self):
        print("Soy una clase A")
    def a(self):
        print("Este metodo lo heredo de la A")
        
        
class B: 
    def __init__(self):
        print("Soy una clase B")
    def b(self):
        print("Este metodo lo heredo de la B")
        
        
class C (A,B):
    def c(self):
        print("Este metodo es del C")
        
        
        
c = C()
c.a()
c.b()
c.c() """







