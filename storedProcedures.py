import tkinter as tk
from tkinter import ttk
def fetch_airlineID (db):
    query = "Select airlineID from airline"
    cursor = db.cursor()
    cursor.execute(query)
    airlines = cursor.fetchall()
    return [airline[0] for airline in airlines]

def fetch_airplane_status (db):
    query = "Select distinct airplane_status from flight"
    cursor = db.cursor()
    cursor.execute(query)
    flights = cursor.fetchall()
    return [flight[0] for flight in flights]

def fetch_flightID (db):
    query = "Select flightID from flight"
    cursor = db.cursor()
    cursor.execute(query)
    flightIDs = cursor.fetchall()
    return [flightID[0] for flightID in flightIDs]

def stored_procedure_offer_flight(db, flightID, routeID, support_airline, support_tail, progress, airplane_status, next_time):
    cursor = db.cursor()
    sql_query = "CALL offer_flight(%s, %s, %s, %s, %s, %s, %s)"
    # query = "call offer_flight('UN_3403', 'westbound_north_milk_run', 'American', 'n380sd', 0, 'on_ground', '15:30:00')"
    parameters = (flightID, routeID, support_airline, support_tail, progress, airplane_status, next_time)
    cursor.execute(sql_query, parameters)
    # cursor.execute(query)
    db.commit()
    result = cursor.fetchall()   

def stored_procedure_flight_landing(db,flightID):
    cursor = db.cursor()
    sql_query = "Call flight_landing(%s)"
    parameters = (flightID,)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()

def stored_procedure_flight_takeoff(db,flightID):
    cursor = db.cursor()
    sql_query = "Call flight_takeoff(%s)"
    parameters = (flightID,)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_retire_flight(db,flightID):
    cursor = db.cursor()
    sql_query = "Call retire_flight(%s)"
    parameters = (flightID,)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_passenger_board(db,flightID):
    cursor = db.cursor()
    sql_query = "Call passengers_board(%s)"
    parameters = (flightID,)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()