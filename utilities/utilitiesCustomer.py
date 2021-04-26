import sqlite3
from  models import CustomerManagement

def RegistrePerson(customer:CustomerManagement):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    info = (customer.IDENTIFICATION,customer.FIRSTNAME,customer.LASTNAME,customer.EMAIL,customer.LICENSE,customer.NATIONALITY,customer.BLOODTYPE,customer.PHOTOPERSON,customer.PHOTOLICENSE)
    registro.execute("INSERT INTO CUSTOMER (IDENTIFICATION, FIRSTNAME, LASTNAME, EMAIL, LICENSE, NATIONALITY, BLOODTYPE, PHOTOPERSON, PHOTOLICENSE) VALUES (?,?,?,?,?,?,?,?,?)",info)
    conexion.commit()

def UpdatePerson(customer:CustomerManagement,IDENTIFICATION:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("UPDATE CUSTOMER SET FIRSTNAME = ?, LASTNAME =?, EMAIL = ?, LICENSE = ?, NATIONALITY = ?, BLOODTYPE = ?, PHOTOPERSON = ?, PHOTOLICENSE =? WHERE IDENTIFICATION= '"+IDENTIFICATION+"' ",(customer.FIRSTNAME,customer.LASTNAME,customer.EMAIL,customer.LICENSE,customer.NATIONALITY,customer.BLOODTYPE,customer.PHOTOPERSON,customer.PHOTOLICENSE))
    conexion.commit()

def AllClient():
    listClients = []
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM CUSTOMER")
    data = registro.fetchall()
    if data !=[]:
        for client in data:
            listClients.append({"ID_CUSTOMER":client[0],"IDENTIFICATION":client[1],"FIRSTNAME":client[2],"LASTNAME":client[3],"EMAIL":client[4],"LICENSE":client[5],"NATIONALITY":client[6],"BLOODTYPE":client[7],"PHOTOPERSON":client[8],"PHOTOLICENSE":client[9],"CONDITION":client[10]})
        return listClients
    else:
        return False

def ClientByIDENTIFICATION(IDENTIFICATION:str):
    listClients = []
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM CUSTOMER WHERE IDENTIFICATION = '"+IDENTIFICATION+"'")
    data = registro.fetchall()
    if data !=[]:
        for client in data:
            return{"ID_CUSTOMER":client[0],"IDENTIFICATION":client[1],"FIRSTNAME":client[2],"LASTNAME":client[3],"EMAIL":client[4],"LICENSE":client[5],"NATIONALITY":client[6],"BLOODTYPE":client[7],"PHOTOPERSON":client[8],"PHOTOLICENSE":client[9],"CONDITION":client[10]}
    else:
        return False

def disableClient(IDENTIFICATION:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("UPDATE CUSTOMER SET CONDITION = 0 WHERE IDENTIFICATION == '"+IDENTIFICATION+"'")
    conexion.commit()

def enableClient(IDENTIFICATION:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("UPDATE CUSTOMER SET CONDITION = 1 WHERE IDENTIFICATION == '"+IDENTIFICATION+"'")
    conexion.commit()

def clientsDebd():
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT C.IDENTIFICATION, C.FIRSTNAME, C.LASTNAME, IFNULL(SUM(P.BILL - P.PAYED), 0) AS 'TOTAL_DEBD' FROM CUSTOMER C LEFT JOIN RESERVATION R ON C.IDENTIFICATION = R.CLIENT LEFT JOIN PAYMENT P ON R.ID_RESERVATION = P.RESERVATION GROUP BY C.IDENTIFICATION")
    data = registro.fetchall()
    if data:
        return [
            dict(zip("IDENTIFICATION","FIRSTNAME","LASTNAME","TOTAL_DEBD"), row)
            for row in data
        ]
    else:
        return False
