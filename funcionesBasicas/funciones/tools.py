import funciones


def multiplicar(num=0):
    for i in range(1,11):
        print(f"{num} x  {i} = {num*i}" )

def operaciones(num1,num2):
    suma=num1+num2
    resta=num1-num2
    return suma,resta

def datosPersona():
    nombre=input("Como te llamas: ")
    edad=input("Cual es tu edad: ")
    direccion=input("Donde vives: ")
    telefono=input("cual es tu telefonos: ")

    persona={
        "nombre":nombre,
        "edad":edad,
        "direccion":direccion,
        "telefono":telefono
    }

    print(f'hola {nombre} tienes {edad} años, vives en {direccion} y tu numero es {telefono}')