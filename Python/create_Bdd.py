#-*- coding: utf-8 -*-
''' Exemple pour IMERIR 3ème année (bac+3) :
    Gestionnaire de la base de données WEATHER

    *   il est nécessaire de lancer ce code une fois en direct afin de créer la
        base de données initiales
        . createBase         crée la base avec sa table des prévisions
        
    *   cette bibliothèque cntient les fonctions nécessaires à la gestion des
        prévisions météorologiques :
        
        . connectBase        connexion à la base de données

        . addForecast        ajouter des prévisions depuis OPENWEATHE
        . forecasts          générateur / liste (filtrée) des prévisions


'''
import sqlite3
from sqlite3 import Error
from pathlib import Path

databaseName = "weather.db"


def connectBase():
    ''' return a connector to the database
    '''
    try:
        conn = sqlite3.connect(databaseName)
        return conn
    except:
        return False
    
def baseExists():
    ''' check if a database exists with the appropriate name
            . we check if the file exists
            . AND we check if we can open it as a sqlite3 database
    '''
    file = Path(databaseName)
    if file.exists () and connectBase():
        return True
    return False

def createBase():
    ''' create the database with the table WEATHER


        WEATHERS is the table of the forecasts
            .town as text
            .longitude as real
            .latitude as real
            .date as text   (date will be YYYYMMDD HH:MM:SS)
            .temp as real
            .temp_min as real
            .temp_max as real
            .humidity as real
            .description as text 
        '''

    #création de la base 
    try:
        conn = sqlite3.connect(databaseName)
    except Error as e:
        quit

    c = conn.cursor()
    c.execute('''CREATE TABLE WEATHERS (
                        town        text,
                        longitude   real,
                        latitude    real,
                        date        text,
                        temp        real,
                        temp_min    real,
                        temp_max    real,
                        humidity    real,
                        description text  )''')
    conn.commit()
    conn.close()

help(createBase)
# Example d'appels
##if not baseExists(): createBase()
##conn = connectBase()
### et on peut utiliser ici le connecteur de la base
