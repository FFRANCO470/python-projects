import vehiculos.database as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Vehiculos:

    #constructor de la clase
    def __init__(self,marca,modelo,precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio

    def guardar(self):
        sql="INSERT INTO vehiculos VALUE (null,%s,%s,%s)"
        vehiculo = (self.marca,self.modelo,self.precio)
        cursor.execute(sql,vehiculo)
        database.commit()
        return [cursor.rowcount,self]

    def listar():
        sql = "SELECT * FROM vehiculos"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def eliminar(id):
        sql = f'DELETE FROM vehiculos WHERE id={id}'
        cursor.execute(sql)
        database.commit()
        return cursor.rowcount