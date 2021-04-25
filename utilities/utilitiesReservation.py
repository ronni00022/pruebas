import sqlite3
from models import ReservationManagement

def createReservation(reservation:ReservationManagement):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("INSERT INTO RESERVATION (VEHICLE, CLIENT, STARDATE, ENDINGDATE)VALUES (?,?,?,?)",(reservation.vehicle,reservation.client,reservation.startdate,reservation.endingdate))
    conexion.commit()

def validateReservation(ending: str,vehicle:str ):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM RESERVATION WHERE VEHICLE = '"+vehicle+"' AND ENDINGDATE> '"+ending+"'")
    return registro.fetchall()
