from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import * 
from utilities import utilitiesUser,utilitiesVehicle,utilitiesCustomer,utilitiesReservation, utilitiesPayment
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
    if validation:
        raise HTTPException(status_code=201, detail="Usuario ya existe")
    utilitiesUser.RegisterUser(user)
    return user

@app.post("/login")
def login(user:Login):
    validation = utilitiesUser.ValidateUser(user)
    if not validation:
        raise HTTPException(status_code=404, detail='Usuario no Existe')
    if validation[4]:
        return {"token": validation[4]}
    token = utilitiesUser.generateToken()
    utilitiesUser.InsertToken(user)
    return {"token": token}

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
    data = utilitiesVehicle.SearchVehicleByEnrollment(vehicle.Enrollment)
    if data:
        raise HTTPException(status_code=201, detail="Esa matricula ya existe")
    utilitiesVehicle.RegisterVehicle(vehicle)
    return {"message":"Registro Exitoso"}

@app.put("/updatevehicle/{enrollment}")
def updatevehicle (vehicle:VehicleRegister,enrollment:str):
    data = utilitiesVehicle.SearchVehicleByEnrollment(enrollment)
    if data == False:
        raise HTTPException(status_code=404, detail="Matricula no existe")
    utilitiesVehicle.UpdateVehicle(vehicle,enrollment)
    return {"message":"Actualizacion Exitosa"}

@app.put("/disableVehicle/{Enrollment}")
def disableVehicle(Enrollment:str):
    utilitiesVehicle.disableVehicle(Enrollment)
    return {"message": "Actualizacion Existosa"}

@app.get("/availableVehicles/{startdate}/{endingdate}")
def availableVehicles(startdate:str, endingdate:str):
    data = utilitiesVehicle.availableVehicles(Dates(Startdate=startdate, Endingdate=endingdate))
    if not data:
        raise HTTPException(status_code=201, detail="No hay vehiculos dispinibles en esa fecha")
    return data

@app.get("/enableVehicles")
def enableVehicles():
    data = utilitiesVehicle.enableVehicles()
    if not data:
        raise HTTPException(status_code=201, detail="No hay vehiculos dispinibles")
    return data

@app.put("/enableVehicle/{Enrollment}")
def enableVehicle(Enrollment:str):
    utilitiesVehicle.enableVehicle(Enrollment)
    return {"message": "Actualizacion Existosa"}

@app.get("/benefitList")
def benefitList():
    data = utilitiesVehicle.benefitList()
    return data

#-----------------CUSTOMER------------------------#
@app.get("/AllClient")
def AllClient():
    data = utilitiesCustomer.AllClient()
    if data==False:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data

@app.get("/getByID/{IDENTIFICATION}")
def getByID(IDENTIFICATION:str):
    data = utilitiesCustomer.ClientByIDENTIFICATION(IDENTIFICATION)
    if data==False:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data

@app.post("/registerCustomer")
def registerCustomer(customer:CustomerManagement):
    utilitiesCustomer.RegistrePerson(customer)
    return {"message":"Registro Existoso"}

@app.put("/updateCustomer/{IDENTIFICATION}")
def updateCustomer(customer:CustomerManagement, IDENTIFICATION:str):
    utilitiesCustomer.UpdatePerson(customer,IDENTIFICATION)
    return {"message":"Actualizacion Exitosa"}

@app.put("/disableClient/{IDENTIFICATION}")
def disableClient(IDENTIFICATION:str):
    utilitiesCustomer.disableClient(IDENTIFICATION)
    return {"message":"Actualizacion Exitosa"}

@app.put("/enableClient/{IDENTIFICATION}")
def enableClient(IDENTIFICATION:str):
    utilitiesCustomer.enableClient(IDENTIFICATION)
    return {"message":"Actualizacion Exitosa"}

@app.get("/clientsDebd")
def clientsDebd():
    data = utilitiesCustomer.clientsDebd()
    return data

#---------------------RESERVATION-------------------#
@app.post("/registrationReservation")
def registrationReservation(reservation:ReservationManagement):
    data = utilitiesReservation.validateReservation(reservation)
    if data:
        raise HTTPException(status_code=201, detail="Vehiculo no disponible")
    utilitiesReservation.createReservation(reservation)
    return {"message":"Registro Existoso"}

#---------------------PAYMENT-------------------#

@app.get("/getAllPayments")
def getAllPayments():
    data = utilitiesPayment.allPayments()
    return data

@app.put("/updatePayment")
def updatePayment(pay:PaymentManagement):
    devuelta = utilitiesPayment.updatePayment(pay)
    if devuelta < 0:
        raise HTTPException(status_code=201, detail="Esa Id no existe")
    return {"message":"Pago actualizado", "devuelta":devuelta}
