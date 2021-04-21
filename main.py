from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import VehicleManagement,CustomerManagement,Login,GestionOfReservs
import utilities
import sqlite3


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}

@app.post("/registeruser")
def postItem(user:Login):
    conexion=sqlite3.connect('app.db')
    registro=conexion.cursor()
    validation = utilities.ValidateRegistration(user.username, user.email)
    if validation == True:
        raise HTTPException(status_code=201, detail="Usuario ya existe")
    registro.execute("INSERT INTO USERS(USERNAME,PASSWORD,EMAIL) VALUES (?,?,?)",(user.username,user.password,user.email))
    conexion.commit()
    return {"message":"Registro exitoso"}
        
    
