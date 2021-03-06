import sqlite3
from  models import VehicleRegister, Dates

def RegisterVehicle(vehicle:VehicleRegister):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    info = (vehicle.BRAND,vehicle.MODEL,vehicle.YEAR,vehicle.COLOUR,vehicle.PRICEPERDAY,vehicle.TYPE,vehicle.LOADCAPACITY,vehicle.PASSENGERS,vehicle.Enrollment,vehicle.INSURANCE_NO,vehicle.PHOTO,vehicle.LATITUDE,vehicle.LONGITUDE)
    query =("INSERT INTO VEHICLE (BRAND, MODEL, YEAR, COLOUR, PRICEPERDAY, TYPE, LOADCAPACITY, PASSENGERS, Enrollment, INSURANCE_NO, PHOTO, LATITUDE, LONGITUDE) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)")
    registro.execute(query,info)
    conexion.commit()

def UpdateVehicle(vehicle:VehicleRegister,enrollment:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    if registro.execute("UPDATE VEHICLE SET BRAND = ?, MODEL = ? , YEAR = ?, COLOUR = ?, PRICEPERDAY = ?, TYPE = ?, LOADCAPACITY = ? ,PASSENGERS = ? , Enrollment = ? , INSURANCE_NO = ? , PHOTO =  ? , LATITUDE = ? , LONGITUDE = ? WHERE Enrollment = '"+enrollment+"'",(vehicle.BRAND,vehicle.MODEL,vehicle.YEAR,vehicle.COLOUR,vehicle.PRICEPERDAY,vehicle.TYPE,vehicle.LOADCAPACITY,vehicle.PASSENGERS,vehicle.Enrollment,vehicle.INSURANCE_NO,vehicle.PHOTO,vehicle.LATITUDE,vehicle.LONGITUDE)):
        conexion.commit()
        return True
    else:
        return False

def SearchVehicleByEnrollment(enrollment:str):
    listData =[]
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM VEHICLE WHERE Enrollment ='"+enrollment+"'")
    data = registro.fetchall()
    if data !=[]:
        for vehicle in data:
            conexion.commit()
            return {"BRAND":vehicle[1],"MODEL":vehicle[2],"YEAR":vehicle[3],"COLOUR":vehicle[4],"PRICEPERDAY":vehicle[5],"TYPE":vehicle[6],"LOADCAPACITY":vehicle[7],"PASSENGERS":vehicle[8],"Enrollment":vehicle[9],"INSURANCE_NO":vehicle[10],"PHOTO":vehicle[11],"LATITUDE":vehicle[12],"LONGITUDE":vehicle[13],"CONDITION":vehicle[14]}
    else:
        return False

def AllVehicle():
    listData =[]
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM VEHICLE")
    data = registro.fetchall()
    if data !=[]:
        for vehicle in data:
            listData.append({"BRAND":vehicle[1],"MODEL":vehicle[2],"YEAR":vehicle[3],"COLOUR":vehicle[4],"PRICEPERDAY":vehicle[5],"TYPE":vehicle[6],"LOADCAPACITY":vehicle[7],"PASSENGERS":vehicle[8],"Enrollment":vehicle[9],"INSURANCE_NO":vehicle[10],"PHOTO":vehicle[11],"LATITUDE":vehicle[12],"LONGITUDE":vehicle[13]})
            conexion.commit()
        return listData
    else:
        return False

def disableVehicle(Enrollment:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("UPDATE VEHICLE SET CONDITION = 0 WHERE Enrollment == '"+Enrollment+"'")
    conexion.commit()

def availableVehicles(dates:Dates):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT V.* FROM VEHICLE V JOIN RESERVATION R ON V.Enrollment = R.VEHICLE WHERE CONDITION IS TRUE AND '{0}' NOT BETWEEN R.STARDATE AND R.ENDINGDATE AND '{1}' NOT BETWEEN R.STARDATE AND R.ENDINGDATE OR R.STARDATE IS NULL".format(dates.Startdate, dates.Endingdate))
    data = registro.fetchall()
    if data:
        return [
            dict(zip(("BRAND","MODEL","YEAR","COLOUR","PRICEPERDAY","TYPE","LOADCAPACITY","PASSENGERS","Enrollment","INSURANCE_NO","PHOTO","LATITUDE","LONGITUDE","CONDITION"), row[1:]))
            for row in data
        ]
    else:
        return False

def enableVehicles():
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM VEHICLE WHERE CONDITION = 1")
    data = registro.fetchall()
    if data:
        return [
            dict(zip(("BRAND","MODEL","YEAR","COLOUR","PRICEPERDAY","TYPE","LOADCAPACITY","PASSENGERS","Enrollment","INSURANCE_NO","PHOTO","LATITUDE","LONGITUDE","CONDITION"), row[1:]))
            for row in data
        ]
    else:
        return False

def enableVehicle(Enrollment:str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("UPDATE VEHICLE SET CONDITION = 1 WHERE Enrollment == '"+Enrollment+"'")
    conexion.commit()

def benefitList():
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT V.*, COUNT(ID_RESERVATION) AS 'TOTAL_RESERVATIONS', IFNULL(SUM(P.BILL), 0) AS 'TOTAL_BILL' FROM VEHICLE V LEFT JOIN RESERVATION R ON V.Enrollment = R.VEHICLE LEFT JOIN PAYMENT P ON R.ID_RESERVATION = P.RESERVATION GROUP BY V.ID_VEHICLE")
    data = registro.fetchall()
    if data:
        return [
            dict(zip(("BRAND","MODEL","YEAR","COLOUR","PRICEPERDAY","TYPE","LOADCAPACITY","PASSENGERS","Enrollment","INSURANCE_NO","PHOTO","LATITUDE","LONGITUDE","CONDITION","TOTAL_RESERVATIONS","TOTAL_BILL"), row[1:]))
            for row in data
        ]
    else:
        return False
