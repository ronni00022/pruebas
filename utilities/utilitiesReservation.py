import sqlite3
from datetime import datetime
from models import ReservationManagement

def createReservation(reservation:ReservationManagement):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("INSERT INTO RESERVATION (VEHICLE, CLIENT, STARDATE, ENDINGDATE)VALUES (?,?,?,?)",(reservation.vehicle,reservation.client,reservation.startdate,reservation.endingdate))

    registro.execute("SELECT ID_RESERVATION FROM RESERVATION ORDER BY ID_RESERVATION DESC LIMIT 1")
    id_reservation=registro.fetchall().pop()[0]

    registro.execute("SELECT PRICEPERDAY FROM VEHICLE WHERE Enrollment = '{0}'".format(reservation.vehicle))
    priceperday=registro.fetchall().pop()[0]

    bill = priceperday * (datetime.strptime(reservation.endingdate, "%Y-%m-%d") - datetime.strptime(reservation.startdate, "%Y-%m-%d")).days

    registro.execute("INSERT INTO PAYMENT (RESERVATION, BILL, PAYED) VALUES (?,?,?)",(id_reservation, bill, 0.0))
    conexion.commit()

def validateReservation(reservation:ReservationManagement):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM RESERVATION WHERE VEHICLE = '"+reservation.vehicle+"' AND ('" + reservation.startdate + "' BETWEEN STARDATE AND ENDINGDATE OR '"+reservation.endingdate+"' BETWEEN STARDATE AND ENDINGDATE)")
    return registro.fetchall()
