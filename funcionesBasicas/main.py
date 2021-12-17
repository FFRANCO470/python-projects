from funciones import saldular,tools
#pylance problemas al imporatr
print(saldular.saludo('nana'))
saludarVar=saldular.saludo
print(saludarVar())

tools.multiplicar(4)

suma,resta = tools.operaciones(55,9)
print(suma)

tools.datosPersona()