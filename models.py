from pydantic import BaseModel
import  datetime

class User(BaseModel):
    username:str
    password:str
    email:str

class Login(BaseModel):
    username: str
    password: str

class VehicleRegister(BaseModel):
    BRAND:str
    MODEL: str
    YEAR: int
    COLOUR: str
    PRICEPERDAY: float
    TYPE: str
    LOADCAPACITY:str
    PASSENGERS: int
    Enrollment:str
    INSURANCE_NO:str
    PHOTO:str
    LATITUDE: str
    LONGITUDE: str

class CustomerManagement(BaseModel):
    IDENTIFICATION:str
    FIRSTNAME:str
    LASTNAME:str
    EMAIL:str
    LICENSE:str
    NATIONALITY:str
    BLOODTYPE:str
    PHOTOPERSON:str
    PHOTOLICENSE:str

class GestionOfReservs(BaseModel):
    VEHICLE: str
    CUSTOMER:str
    STARTDATE:str
    ENDINGDATE:str

class AllUpdate(BaseModel):
    Id: str
    campo:str
    valor:str

class ReservationManagement(BaseModel):
    vehicle: str
    client: str
    startdate: str
    endingdate: str

class PaymentManagement(BaseModel):
    PaymentId: str
    Pay: float
