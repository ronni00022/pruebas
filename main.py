from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import VehicleRegister,CustomerManagement,Login,GestionOfReservs,User
from utilities import utilitiesUser,utilitiesVehicle,utilitiesCustomer
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

#---------------------Login AND REGISTRATION-----------------#
@app.post("/registeruser",response_model=User)
def postItem(user:User, status_code=200):
    validation = utilitiesUser.ValidateRegistration(user)
    if validation == True:
        raise HTTPException(status_code=201, detail="Usuario ya existe")
    utilitiesUser.RegisterUser(user)
    return user

@app.post("/login")
def login(user:Login):
    validation = utilitiesUser.ValidateUser(user)
    if validation == False:
        raise HTTPException(status_code=404, detail='Usuario no Existe')
    return {"token": validation}

#----------------------VEHICLE---------------------------#

@app.get("/SearchEnrollment/{enrollment}")
def SearchEnrollment(enrollment:str):
    data = utilitiesVehicle.SearchVehicleByEnrollment(enrollment)
    if data == False:
        raise HTTPException(status_code=404, detail="Matricula no existe")
    return data
@app.get("/AllVehicle")
def SearchEnrollment():
    data = utilitiesVehicle.AllVehicle()
    if data == False:
        raise HTTPException(status_code=404, detail="Matricula no existe")
    return data

@app.post("/registervehicle")
def registervehicle(vehicle:VehicleRegister):
    utilitiesVehicle.RegisterVehicle(vehicle)
    return {"message":"Registro Exitoso"}

@app.put("/updatevehicle/{enrollment}")
def updatevehicle (vehicle:VehicleRegister,enrollment:str):
    data = utilitiesVehicle.SearchVehicleByEnrollment(enrollment)
    if data == False:
        raise HTTPException(status_code=404, detail="Matricula no existe")
    utilitiesVehicle.UpdateVehicle(vehicle,enrollment)
    return {"message":"Actualizacion Exitosa"}

#-----------------CUSTOMER------------------------#
@app.post("/registerCustomer")
def registerCustomer(customer:CustomerManagement):
    utilitiesCustomer.RegistrePerson(customer)
    return {"message":"Registro Existoso"}

@app.put("/updateCustomer/{Id}")
def updateCustomer(customer:CustomerManagement, Id:str):
    utilitiesCustomer.UpdatePerson(customer,Id)
    return {"message":"Actualizacion Exitosa"}




        
    
