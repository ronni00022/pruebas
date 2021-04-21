from pydantic import BaseModel

class Login(BaseModel):
    username:str
    password:str
    email:str

class VehicleManagement(BaseModel):
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

