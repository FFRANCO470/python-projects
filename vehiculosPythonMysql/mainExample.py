# #### libreria para conectar a mysql
# import mysql.connector

# #### conectarse con la base de datos
# database = mysql.connector.connect(
#     #direccion de la base de datos
#     host = "localhost",
#     user="root",
#     passwd="",
#     #nombre de la base de datos
#     database="adsi2067725"
# )
# #### para operar sobre la base de datos (buffered es para que almacene en una memoria caceh -no seguro-)
# cursor = database.cursor(buffered=True)
#### DML : manipular datos insert into , delete, update, select
#### DDL: modifica la estructura de la bd create tabla

#### crear base de datos
#cursor.execute("CREATE DATABASE adsi2067725")
#cursor.execute("CREATE DATABASE IF NOT EXISTS adsi2067725")

# #### listar base de datos
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)

#### crear tabla en la base de datos
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS vehiculos(
#     id int(10) auto_increment not null,
#     marca varchar(40) not null,
#     modelo varchar(40) not null,
#     precio float(10,2) not null,
#     CONSTRAINT pk_vehiculo PRIMARY KEY(id)
# )
# """)

# ### listar las tablas
# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table)

#### insertar un registro a la base de datos
#cursor.execute("INSERT INTO vehiculos (marca,modelo,precio) VALUES ('Toyota','Rav4',12345")
#cursor.execute("INSERT INTO vehiculos VALUES (null,'Toyota','Rav4',12345)")
#database.commit()

#### insertar varios registros a la base de datos
# coches=[
#     ('For','4x4',15000),
#     ('Miszubichi','CVD',45000),
#     ('MERCEDEZ','BEN',40333)
# ]
# #%s son parametros
# cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)
# database.commit()

# ### seleccionar datos de una tabla
# cursor.execute("SELECT * FROM vehiculos")
# result = cursor.fetchall()
# print('---- lista de vehiculos ----')
# for item in result:
#     print(item)
#     print(item[2])
# database.commit()

# ### seleccionar datos de una tabla con condición
# cursor.execute("SELECT * FROM vehiculos WHERE id=2")
# result = cursor.fetchall()
# for item in result:
#     print(item[2])
# database.commit()

# #### seleccionar datos que comiencen por c
# cursor.execute("SELECT * FROM vehiculos WHERE modelo like 'C%'")
# result = cursor.fetchall()
# for item in result:
#     print(item[1])
# database.commit()

# #### seleccionar los datos que contengan la a
# cursor.execute("SELECT * FROM vehiculos WHERE  marca like '%a%'")
# result = cursor.fetchall()
# for item in result:
#     print(item[1])
# database.commit()

# #### seleccionar datos con varias condiciones
# cursor.execute("SELECT * FROM vehiculos WHERE marca like '%a%' and modelo like 'C%'")
# result = cursor.fetchall()
# for item in result:
#     print(item[1], item[2])
# database.commit()

# #### actualizar todos los campos modelo con cxs
# cursor.execute("UPDATE vehiculos SET modelo='CXS'")

# #### actualiar los campos modelo con cxs de los registros que tengan mazda en su campo marca  
# cursor.execute("UPDATE vehiculos SET modelo='CXS' WHERE marca='Mazda'")
# database.commit()

# #### actualizar y mostrar
# cursor.execute("UPDATE vehiculos SET modelo='Capture' WHERE id=3")
# cursor.execute("SELECT * FROM vehiculos")
# result = cursor.fetchall()
# for item in result:
#     print(item[1],item[2])
# database.commit()

# #### borrar todo dentro de la tabla vehiculos
# cursor.execute ("DELETE FROM vehiculos")
# database.commit()

# #### borrar los registros que tengan mercedez en el campo marca 
# cursor.execute("DELETE FROM vehiculos WHERE marca='Mercedez'")
# print(cursor.rowcount,"     borrados")
# database.commit()


# #### controlar errores
# try:
#     numero = int(input('numero para elevar al cuadrado:   '))
#     print(f'el numero al cuadrado es:  {numero*numero}')
# except:
#     #hay un error
#     print('no ingreso un numero entero')
# else:
#     #no hay error
#     print('todo funciono bien')
# finally:
#     #alla o no error se ejecuta
#     print('fin de la instruccion')





try:
    age = int(input('enter your age:  '))
    if age <1 or age>100:
        #crear error
        raise ValueError('invalid age')
except Exception as e:
    print('exception invalid age')
    print(e)
finally:
    print('ended process')
