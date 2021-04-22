import sqlite3
from  models import CustomerManagement

def RegistrePerson(customer:CustomerManagement):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    info = (customer.IDENTIFICATION,customer.FIRSTNAME,customer.LASTNAME,customer.EMAIL,customer.LICENSE,customer.NATIONALITY,customer.BLOODTYPE,customer.PHOTOPERSON,customer.PHOTOLICENSE)
    registro.execute("INSERT INTO CUSTOMER (IDENTIFICATION, FIRSTNAME, LASTNAME, EMAIL, LICENSE, NATIONALITY, BLOODTYPE, PHOTOPERSON, PHOTOLICENSE) VALUES (?,?,?,?,?,?,?,?,?)",info)
    conexion.commit()

def UpdatePerson(customer:CustomerManagement,Id:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("UPDATE CUSTOMER SET FIRSTNAME = ?, LASTNAME =?, EMAIL = ?, LICENSE = ?, NATIONALITY = ?, BLOODTYPE = ?, PHOTOPERSON = ?, PHOTOLICENSE =? WHERE IDENTIFICATION= '"+Id+"' ",(customer.FIRSTNAME,customer.LASTNAME,customer.EMAIL,customer.LICENSE,customer.NATIONALITY,customer.BLOODTYPE,customer.PHOTOPERSON,customer.PHOTOLICENSE))
    conexion.commit()


