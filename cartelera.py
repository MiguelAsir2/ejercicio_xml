from lxml import etree
doc=etree.parse('cartelera.xml')
from funcionescartelera import nombre_pelicula
from funcionescartelera import nombre_cine
from funcionescartelera import direccion_cine
from funcionescartelera import municipio_cine
from funcionescartelera import opciones_categoria
cont=0
pelis=[]
categoria=[]
cont1=0
sinop=[]
#Programa principal
while True:
    #Menu
    print()
    print ('''1. Muestra el listado de peliculas
2. Introduce género y te muestras cuantas peliculas hay de ese tipo.
3. Introduce pelicula y muestra el cine y localización.
4. Introduce pelicula y muestra la sinopsis
5. Introduce pelicula y muestra el cine y los horarios
0. Salir''')
    opcion=int(input("Introduce el número de la opción: "))
    if opcion<0 or opcion>5:
        print("No es una opcion válida para este menú")
    if opcion==1:
        for i in nombre_pelicula(doc):
            pelis.append(i)
            if pelis.count(i)>1:
                pelis.remove(i)
        for i in pelis:
            print(i)
   
