-- SQLite --
create table VEHICLE(
ID_VEHICLE INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
BRAND TEX,
MODEL TEXT,
YEAR INT,
COLOUR TEXT,
PRICEPERDAY REAL,
TYPE TEXT,
LOADCAPACITY TEXT,
PASSENGERS INT,
Enrollment TEXT,
INSURANCE_NO TEXT,
PHOTO TEXT,
LATITUDE REAL,
LONGITUDE REAL,
CONDITION BOOL DEFAULT FALSE
)

CREATE TABLE CUSTOMER(
ID_CUSTOMER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
IDENTIFICATION TEXT,
FIRSTNAME TEXT,
LASTNAME TEXT,
EMAIL TEXT,
LICENSE TEXT,
NATIONALITY TEXT,
BLOODTYPE TEX,
PHOTOPERSON TEXT,
PHOTOLICENSE TEX,
CONDITION BOOL DEFAULT TRUE
)

CREATE TABLE BOOKINGS(
ID_BOOKINGS INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
VEHICLE TEXT,
CUSTOMER TEXT,
STARTDATE TEXT,
ENDINGDATE TEXT,
CONDITION BOOL DEFAULT TRUE
)

CREATE TABLE USERS(
ID_USER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
USERNAME TEXT,
PASSWORD TEXT,
EMAIL TEXT,
TOKEN TEXT
)

CREATE TABLE RESERVATION(
ID_RESERVATION INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
VEHICLE TEXT,
CLIENT TEXT,
STARDATE TEXT,
ENDINGDATE TEXT
)

CREATE TABLE PAYMENT(
ID_PAYMENT INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
RESERVATION TEXT,
BILL REAL,
PAYED REAL
)
