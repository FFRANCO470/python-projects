def saludar(name=''):
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

def precioFruta():
    frutas={
        'platano':1.35,
        'manzana':0.8,
        'pera':0.85,
        'naranja':0.7
    }
    fruta=input("Ingrese la futra: ")
    if fruta in frutas:
        kilos=int(input('Ingrese cantidad en kilos (ejem:5.5):  '))   
        total = kilos * frutas[fruta]
        print (f'el total de {fruta} es {total}')
    else:
        print (f'{fruta} no existe')

def carrito():
    frutas={
        'platano':1.35,
        'manzana':0.8,
        'pera':0.85,
        'naranja':0.7
    }
    fruta=''
    total=0
    frutasCompradas=[]
    print('frutas a la venta')
    print('_______________________')
    for item in frutas:
        print(f'{item}')
    print('_______________________')
    while fruta!='facturar':
        fruta = input('Ingrese la fruta o "facturar" para salir:    ')
        if fruta in frutas:
            kilo = float(input('Ingrese los kilos (eje: 3.3):    '))
            subtotal = kilo * frutas[fruta]
            total = total + subtotal
            frutaComprada = {"fruta":fruta,"subtotal":subtotal}
            frutasCompradas.append(frutaComprada)
        else:
            if fruta!='facturar':
                print(f'no existe {fruta}')
    print('____________productos comprados___________')
    for frutillas in frutasCompradas:
        print(f' {frutillas["fruta"]} costo {frutillas["subtotal"]} ')
    print('_______________________')
    print(f'total vendido {total}')
    return total

def inversos():
    number = list(range(1,11))
    number.reverse()
    print(number)

def priemroUltimo():
    number = [50, 75, 46, 22,80, 65, 8]
    print(number)
    number.sort()
    primero = number[0]
    ultimo = number[-1]
    print(f'menor {primero} y mayor {ultimo}')

def mediana():
    lista = input('ingrese la lista de numeros (eje: 2,4,3):   ')
    lista = lista.split(',')
    print(lista)
    cantidad = len(lista)
    total=0
    print(cantidad)
    for num in lista:
        total = total+float(num)
    media = total/cantidad
    print(media)

def ivaFuntion(iva=0.19):
    total = carrito()
    print(f'iva {iva}')
    print(f'valor iva:  {total*iva}')
    print(f'valor total:  {total + (total*iva)}')

def cuadrados():
    lista = input('ingrese la lista de numeros (eje: 2,4,3):   ')
    lista = lista.split(',')
    listaNew =[]
    for item in lista:
        numero = int(item)**2
        listaNew.append(numero)
    print(lista)
    print(listaNew)

def multiplicar():
    num = int(input('Ingrese un numero:   '))
    for i in range(1,11):
        print(f"{num} x  {i} = {num*i}" )