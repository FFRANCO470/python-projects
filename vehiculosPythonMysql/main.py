import vehiculos.vehiculosModel as modelo

# vehiculo = modelo.Vehiculos("Renault","Megane",11000)
# print(vehiculo)

# guardar  = vehiculo.guardar()
# print(guardar[0])

lista = modelo.Vehiculos.listar()
print(lista)

eliminar = modelo.Vehiculos.eliminar(3)
print(eliminar)

lista = modelo.Vehiculos.listar()
print(lista)





