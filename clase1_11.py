""" lista = []
if len(lista) > 0:
    lista.pop()

 """


#TRY / EXCEPT

""" while(True):
    try:
        n = float(input("Ingresa un numero: "))
        m = 10
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ocurrió un error. Ingresaste algo que no era un numero.")
    else:
        print("Todo salio bien")
        break
    finally:
        print("Este es el fin")      """
        
"""     
try:
    n=input("Introduce un numero: ")
    5/n
except Exception as e:
    print("Ha ocurrido un error", type(e).__name__ )


    
print(type(1).__name__) """

""" 
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError ("Error! Otra vez!")
    except ValueError:
        print("El mismo error, pero desde la excepción")
mi_funcion()
 """


#POO
#CLASES


""" class Calzado:
    pass


un_calzado = Calzado()
otro_calzado = Calzado()

print(Calzado.__name__)
print(type(un_calzado))
 """

#ATRIBUTOS

""" class Zapatilla:
    pass
zapatilla = Zapatilla()
zapatilla.color = "Negra"
zapatilla.cordones = "Con cordones"

print(f"El color de la zapatilla es {zapatilla.color}" f", la zapatilla viene {zapatilla.cordones}") """


""" class Zapatilla:
    con_cordones = False
    
Zapatilla.con_cordones = True    
zapatilla = Zapatilla()

if zapatilla.con_cordones:
    print("La zapas vienen con cordones")
else:
    print("Las zapas no vienen con cordones") """

#METODOS    

""" class Zapatilla:
    con_cordones = False
    
    def saludar(este_es_el_self):
        print("Soy una zapatilla")
        print(este_es_el_self)

zapatilla = Zapatilla()
zapatilla.saludar() """





class Zapato:
    cuero = False
    
    def zapatosdecuero(self):
        self.cuero = True
        
cuero = Zapato()
cuero.zapatosdecuero()
print(cuero.cuero)

