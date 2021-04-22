import sqlite3
from  models import VehicleRegister

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
            listData.append({"BRAND":vehicle[1],"MODEL":vehicle[2],"YEAR":vehicle[3],"COLOUR":vehicle[4],"PRICEPERDAY":vehicle[5],"TYPE":vehicle[6],"LOADCAPACITY":vehicle[7],"PASSENGERS":vehicle[8],"Enrollment":vehicle[9],"INSURANCE_NO":vehicle[10],"PHOTO":vehicle[11],"LATITUDE":vehicle[12],"LONGITUDE":vehicle[13]})
            conexion.commit()
        return listData
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



