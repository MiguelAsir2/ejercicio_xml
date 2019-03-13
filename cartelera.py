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
    elif opcion==2:
        for i in opciones_categoria(doc):
            categoria.append(i)
        for i in categoria:
            while categoria.count(i)>1:
                categoria.remove(i)
        for i in categoria:
            cont1+=1
            print("%d. %s"%(cont1,i))         
        nombre_categoria=input("Introduce una categoria de pelicula: ")
        if nombre_categoria not in categoria:
            print("Esa categoría no existe en estas películas")
        if nombre_categoria in categoria:
            for i in categoria:
                cont=cont+1
            print("De la categoria %s hay %d peliculas"%(nombre_categoria,cont))
        cont1=0     
 	elif opcion==3:
        nombre_pelis=input("Introduce el nombre de una pelicula: ")
        nombre_cines=doc.xpath('//cartelera/cine/pelicula[@titulo="%s"]/../@nombre'%nombre_pelis)
        if nombre_pelis in nombre_pelicula(doc):
            for i in nombre_cines:
                print(i)
                cont+=1
            direccion=input("¿Desea saber su localizacion(S/N)? ")
            if direccion.upper()=="S":
                for i in nombre_cines:
                    print("%s se encuentra en "%i,end="")
                    for i in doc.xpath('//cartelera/cine[@nombre="%s"]/@direccion'%i):
                        print(i)
    elif opcion==4:
        for i in nombre_pelicula(doc):
            pelis.append(i)
            if pelis.count(i)>1:
                pelis.remove(i)
        for i in pelis:
            print(i)
        pelicula=input("Introduce el nombre de una pelicula: ")
        sinopsis=doc.xpath('//cartelera/cine/pelicula[@titulo="%s"]/sinopsis/text()'%pelicula)
        if pelicula in nombre_pelicula(doc):
            for i in sinopsis:
                sinop.append(i)
            while sinop.count(i)>1:
                sinop.remove(i)
            print(i)
        else:
            print("Esta película no está disponible")
    elif opcion==5:
        pelicula=input("Introduce el nombre de una película: ")
        nombre_cines=doc.xpath('//cartelera/cine/pelicula[@titulo="%s"]/../@nombre'%pelicula)
        print("La película %s se encuentra en:"%pelicula)
        for i in nombre_cines:
            print(i)
        print()
        print("Horarios:")
        print()
        dias=doc.xpath('//cartelera/cine/pelicula[@titulo="%s"]/sesiones/sesion/@dia'%pelicula)
        horas=doc.xpath('//cartelera/cine/pelicula[@titulo="%s"]/sesiones/sesion/@hora'%pelicula)
        for i,j in zip(dias,horas):
            print(i,"-->",end="")
            print(j)
    if opcion==0:
        break 
print()
