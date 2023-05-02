import tkinter as tk
from tkinter import ttk

def fetch_personID (db):
    query = "Select personID from person"
    cursor = db.cursor()
    cursor.execute(query)
    persons = cursor.fetchall()
    return [person[0] for person in persons]

def fetch_license_type (db):
    query = "Select distinct license from pilot_licenses"
    cursor = db.cursor()
    cursor.execute(query)
    pilot_licenses = cursor.fetchall()
    return [pilot_license[0] for pilot_license in pilot_licenses]

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

def stored_procedure_grant_pilot_license (db, personID, license):
    cursor =db.cursor()
    sql_query = "CALL grant_pilot_license(%s, %s)"
    parameters = (personID, license)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_assign_pilot (db, flightID, personID):
    cursor =db.cursor()
    sql_query = "CALL assign_pilot(%s, %s)"
    parameters = (flightID, personID)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_recycle_crew (db, flightID):
    cursor =db.cursor()
    sql_query = "CALL recycle_crew(%s)"
    parameters = (flightID)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_remove_pilot_role (db, personID):
    cursor =db.cursor()
    sql_query = "CALL remove_pilot_role(%s)"
    parameters = (personID)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_passengers_disembark (db, flightID):
    cursor =db.cursor()
    sql_query = "CALL passengers_disembark(%s)"
    parameters = (flightID)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()

def stored_procedure_remove_passenger_role (db, personID):
    cursor =db.cursor()
    sql_query = "CALL remove_passenger_role(%s)"
    parameters = (personID)
    cursor.execute(sql_query, parameters)
    db.commit()
    result = cursor.fetchall()
    db.commit()






