#1) Trabajemos con listas y tuplas

#Crea una lista y una tupla que contenga strings (al menos 3 elementos). Tematica libre, sobre lo que quieras, vehiculos, comida, música, etc.
vehiculos = ["coche","moto","camión","bicicleta"] #lista vehículos
musica = ("clásica","pop","rock") #tupla música (inmutable)

#Muestra la lista y la tupla
print(vehiculos)
print(musica)

#Muestra el 2º elemento de la lista y el penúltimo de la tupla
print(vehiculos[1])
print(musica[-2])

#Modifica (si se puede) algún elemento de la lista y de la tupla. Y mostrar el resultado
vehiculos.remove("camión")
vehiculos.insert(2,"avión")
print(vehiculos) #las tuplas son inmutables por lo que no podemos modificar sus elementos

#Muestra el tamaño de la lista y de la tupla
print("La lista tiene",len(vehiculos), "elementos.")
print("La tupla tiene",len(musica), "elementos.")

#Realiza una búsqueda de un elemento dentro de la lista y de la tupla. Mostrar si devuelve True o False
buscar = input("Introduzca el elemento a buscar: ")

posiciones = []  # nuestra lista para guardar las posiciones
posicion = 0  # empezaremos a buscar en la primera posición (que es el índice 0)

try:
    while True:
        # buscamos empezando a buscar desde la última posición encontrada
        posicion = vehiculos.index(buscar, posicion + 1)
        posiciones.append(posicion)
except:
    pass  # no hacemos nada si index lanza ValueError

print(posiciones)

#Añade (si se puede) algún elemento a la lista y a la tupla. Mostrar de nuevo la lista y la tupla para verificar si se ha realizado correctamente la acción.
vehiculos.append("bus")
print(vehiculos) #las tuplas son inmutables por lo que no podemos modificar sus elementos

#Borra o elimina (si se puede) el contenido de la lista y de la tupla. Mostrar de nuevo la lista y la tupla para verificar si se ha realizado correctamente la acción.
vehiculos=[]
print(vehiculos) #las tuplas son inmutables por lo que no podemos eliminar sus elementos


#2) Trabajemos con sets y diccionarios

#Crea una set y un diccionario que contengan strings (al menos 3 elementos en el caso del set y 3 conjuntos de clave:valor en el caso del diccionario). Tematica libre, sobre lo que quieras, vehiculos, comida, música, etc.
diccionario = {
'Nombre' : 'David',
'Apellido' : 'Ruiz',
'Padres' : ["Pedro Ruiz", "Rafaela Luque"],
'Edad' : 19,
'Genero' : 'Masculino'
}

lenguajes = {"Python", "C++", "Javascript"}

