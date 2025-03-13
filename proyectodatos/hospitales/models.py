from django.db import models
import oracledb

# Create your models here.
class Departamento:
    numero = 0
    nombre = ""
    localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
    
    def insertarDepartamento(self, numero, nombre, localidad):
        sql = "insert into DEPT values (:p1, :p2, :p3)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def eliminarDepartamento(self, numero):
        sql = "delete from DEPT where DEPT_NO = :p1)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        self.connection.commit()
        cursor.close()

    def getDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            dept = Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            lista.append(dept)
        cursor.close()
        return lista
    
class Hospital:
    hospitalCod = 0
    nombre = ""
    direccion = ""
    telefono = 0
    numCama = 0

class ServiceHospitales:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
    
    def getHospitales(self):
        sql = "select * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            hosp = Hospital()
            hosp.hospitalCod = row[0]
            hosp.nombre = row[1]
            hosp.direccion = row[2]
            hosp.telefono = row[3]
            hosp.numCama = row[4]
            lista.append(hosp)
        cursor.close()
        return lista