import sqlite3
def ValidateUser(user: str, password: str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (user, password))
    if registro.fetchall():
        return False
    else:
        return True
def ValidateRegistration(user: str, email: str):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM USERS WHERE USERNAME = ? OR EMAIL = ?", (user,email))
    if registro.fetchall():
        return True
    else:
        return False


    
