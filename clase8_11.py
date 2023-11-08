""" class Galletita:
    chocolate = False
    
    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galletita")
        print(soy_el_propio_objeto)
        
galleta = Galletita()
galleta.saludar()



class Galletita:
    chocolate = False
    
    def chocolatear(self):
        self.chocolate = True
        
galleta = Galletita()
galleta.chocolatear()
print(galleta.chocolate)



class Galletita:
    def __init__(self):
        print("Hola, soy una galleta esta vez")
    
galleta = Galletita()

""" 
##CONSTRUCTOR """

class Galletita:
    chocolate = False
    
    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print(f'Se creo una galletita {self.color} y {self.sabor}')

galletita_1 = Galletita("Marron", "amarga")
galletita2 = Galletita("Negra", "Dulce")



class Galletita:
    def __del__(self):
        print("Me estoy borrando")
        
galleta = Galletita()

del(galleta)    


""" galleta.__del__() """



class Galletita:
    
    def __init__(self,sabor,color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
        return f"Soy una galletita {self.color} y {self.sabor}"
    
galleta = Galletita("Dulce", "Rosa")

print(galleta)
print(str(galleta))
print(galleta.__str__())



class Cancion:
    def __init__(self, autor, titulo, duracion): 
        self.duracion = duracion
        
    def __len__(self):
        return self.duracion
    
cancion = Cancion("Conejo Malo", "Titi me pregunto", 420)

print(len(cancion))

print(cancion.__len__())




class Pelicula:
    #Contructor de clase
    def __init__(self, titulo, duracion, director):
        self.titulo = titulo
        self.duracion = duracion
        self.director = director
        print("Alquilamos la pelicula: ", self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.director)
    
class Catalogo:
    peliculas = [] # En esta lista, la idea es que esten los objetos de la clase Pelicula
    
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
        
    def agregar(self, peli): #Aca peli sera el objeto Pelicula
        self.peliculas.append(peli)
        
    def mostrar(self):
        for peli in self.peliculas:
            print(peli)
            
            
peli = Pelicula("El señor de los Anillos", 185,"Peter Jackson")
c = Catalogo([peli])
c.mostrar()
c.agregar(Pelicula("El señor de los Anillos: Las dos torres", 202, "Peter Jackson")) #Estamos agragando otra, porque usamos el .append
c.mostrar()



""" 
class Ejemplificando:
    __estoesunatributoprivado = "De esta forma lo hacemos inaccesible"
    
e = Ejemplificando()
print(e.__estoesunatributoprivado)
 """


class Ejemplificando:
    def __estoesunmetodoprivado(self):
        print("Yo tambien son inaccesible")
        
e = Ejemplificando()
print(e.__estoesunmetodoprivado())
