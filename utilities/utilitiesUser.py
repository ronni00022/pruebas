import sqlite3
import secrets
from  models import Login,User

def ValidateUser(user:Login):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (user.username,user.password))
    return registro.fetchall()
    

def ValidateRegistration(user:User):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("SELECT * FROM USERS WHERE USERNAME = ? OR EMAIL = ?", (user.username,user.email))
    return registro.fetchall()

def generateToken():
    token = secrets.token_hex(20)
    return token

def InsertToken(user:Login):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    token = generateToken()
    registro.execute("UPDATE USERS SET TOKEN = '"+token+"' WHERE USERNAME = ? AND PASSWORD = ? ",(user.username,user.password))
    conexion.commit()
    return token


def RegisterUser(user:User):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    registro.execute("INSERT INTO USERS(USERNAME,PASSWORD,EMAIL) VALUES (?,?,?)",(user.username,user.password,user.email))
    conexion.commit()