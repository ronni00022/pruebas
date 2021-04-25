import sqlite3
from models import PaymentManagement

def updatePayment(pay:PaymentManagement):
    conexion = sqlite3.connect("app.db")
    registro = conexion.cursor()
    registro.execute("SELECT BILL, PAYED FROM PAYMENT WHERE ID_PAYMENT = '%s'" % pay.PaymentId)
    data = registro.fetchall()

    if not data:
        return -1

    bill, payed = data.pop()
    res = 0.0

    if (pay.Pay + payed) >= bill:
        registro.execute("UPDATE PAYMENT SET PAYED = %s WHERE ID_PAYMENT = '%s'" % (bill, pay.PaymentId))
        res = pay.Pay - (bill - payed)
    else:
        registro.execute("UPDATE PAYMENT SET PAYED = PAYED + %s WHERE ID_PAYMENT = '%s'" % (pay.Pay, pay.PaymentId))

    conexion.commit()
    return res

def allPayments():
    conexion = sqlite3.connect("app.db")
    registro = conexion.cursor()
    registro.execute("SELECT * FROM PAYMENT")
    data = registro.fetchall()
    if data:
        return [dict(zip(("ID_PAYMENT", "RESERVATION", "BILL", "PAYED"), row)) for row in data]
    return {}
