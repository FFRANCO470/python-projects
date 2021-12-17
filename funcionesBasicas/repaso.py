# ####funcion basica
# def saludar():
#     print('funcion basica')
# saludar()

# ####funcion con parametros
# def saludar2(nombre):
#     print(f'saludar a {nombre}')
# saludar2('Nana')

# ####funcion con parametro predeterminado
# def saludar3(nombre='Faramis'):
#     print(f'Saludar a {nombre}')
# saludar3()

# ####funcion con retarno
# def saludar4(nombre='Natan'):
#     return f'Saludar a {nombre}'
# saludar5 = saludar4()
# print (saludar5)

# ####funcion con varios retornos
# def operaciones(num1,num2):
#     suma = num1 + num2
#     resta = num1 - num2
#     return suma,resta
# x , y = operaciones(10,5)
# print(f'la suma es {x} y la resta es {y}')

# ####funcion lambda (1 parametro)
# sumar = lambda year:f'El nuevo año es {year+2}'
# print(sumar(2021))

# #### lista basica
# variada = ['Faramis', 125, False]
# print(variada)

# ##### operando con lista
# semana = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
# #semana = [-7,-6,-5,-4,-3,-2,-1]
# print(semana[-3])

# #cambiar valor de posicion
# semana[0] = 'fiesta'
# semana[-1] = 'fiesta'
# print(semana)

# #cambiar varios valores
# semana2 = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
# semana2[0] = semana2[1] = semana2[2] = 'fiesta'
# print(semana2)

# #seleccionar rangos (el ultimo no lo toma)
# print(semana[1:4])
# print(semana[3:])

# #agregar al final
# semana.append('otro dia')
# print(semana)

# #agregar en cualquier posicion(desplaza de izquierda a derecha)
# semana.insert(3,'posicion')
# print(semana)

# #llenar lista con rangos (no incluye el ultimo)
# years = list(range(2020,2030))
# print(years)

# #eliminar posicion
# years.pop(1)
# years.pop()
# print(years)

# #recorrer lista
# for dia in semana:
#     print(f'hoy es {dia}')

# #### ciclo white
# movies = []
# newMovies = ''
# while newMovies!='parar':
#     newMovies=input('Insestar pelicula:   ')
#     if(newMovies!='parar'):
#         movies.append(newMovies)
# print(movies)

# #indice de un elemento de una lista
# movies = ['la monja', 'el aro', 'caminos del terror', 'el coleccionista', 'sawl']
# for movie in movies:
#     print(f'{movies.index(movie)} -> {movie}')

# ####matrices
# contactos = [
#     ['faramis','mago',3],
#     ['nana','apoyo',2],
#     ['natan','adc',1]
# ]

# print(contactos[2][2])
# print(contactos[0][0])
# #recorrer matriz
# for contacto in contactos:
#     print(f'{contacto}')
#     for item in contacto:
#         print(f'{item}')

# #### ordenar una lista
# numbers = [1,6,4,3,-6,3,7,3,0,3,3]
# numbers.sort()
# print(numbers)

# #volverlo al reves (el ultimo sera el primero)
# numbers.reverse()
# print(numbers)

# #contar un valor en una lista
# print(numbers.count(3))

# #unir dos listas
# contactos = [
#     ['faramis','mago',3],
#     ['nana','apoyo',2],
#     ['natan','adc',1]
# ]
# contactos.extend(numbers)
# print(contactos)


#### diccionarios = objetos (js)
# person = {
#     "name" :"nana",
#     "lastName":"natan",
#     "age":45,
#     "mayor":False
# }
# print(person)
# print(person["name"])

# #cambiar valor de diccionario
# person["age"] = 70
# print(person)

# #cambiar diccionario a un diccionario
# person["hobies"]={
#     "atletismo":"si",
#     "futbol":"no"
# }
# print(person)
# print(person["hobies"]['futbol'])

# ####validar diccionario
# person = {
#     "name" :"nana",
#     "lastName":"natan",
#     "mayor":False,
# }
# if 'age' in person:
#     print(person["age"])
# #optener claves
# x = person.keys()
# print(x)
# for item in x :
#     print(item)

#### listas y diccionarios
# contactos=[
#     {'name':'nana','rol':'mago'},
#     {'name':'natan','rol':'adc'},
#     {'name':'hanzo','rol':'ass'}
# ]
# for contacto in contactos:
#     print(contacto['name'])
    