import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def fetch_personID (db):
    query = "Select personID from person"
    cursor = db.cursor()
    cursor.execute(query)
    persons = cursor.fetchall()
    return [person[0] for person in persons]

def fetch_airportID (db): #departure, arrival, ariportid
    query = "Select airportID from airport"
    cursor = db.cursor()
    cursor.execute(query)
    airports = cursor.fetchall()
    return [airport[0] for airport in airports]

def fetch_locationID (db): #departure, arrival, ariportid
    query = "Select locationID from location"
    cursor = db.cursor()
    cursor.execute(query)
    locations = cursor.fetchall()
    return [location[0] for location in locations]

def fetch_ticketID (db): 
    query = "Select ticketID from ticket"
    cursor = db.cursor()
    cursor.execute(query)
    tickets = cursor.fetchall()
    return [ticket[0] for ticket in tickets]

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

def fetch_plane_state(db, flightID):
    cursor = db.cursor()
    query = "SELECT airplane_status FROM flight WHERE flightID = %s"
    parameters = (flightID,)
    cursor.execute(query, parameters)
    result = cursor.fetchone()
    return result[0] if result else None

#6
def stored_procedure_purchase_ticket_and_seat(db, ticketID, cost, carrier, customer, deplane_at, seat_number):
    cursor = db.cursor()
    if not ticketID:
        messagebox.showerror("Error", "Ticket ID cannot be empty.")
        return
    try:
        parameters = (ticketID, cost, carrier, customer, deplane_at, seat_number)
        cursor.callproc("purchase_ticket_and_seat", parameters)
        db.commit()
        messagebox.showinfo("Success", "Ticket booked successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error purchasing ticket/seat: {e}")
    finally:
        cursor.close()

#7
def stored_procedure_update_leg(db, legID, distance, departure, arrival):
    cursor = db.cursor()
    if not legID:
        messagebox.showerror("Error", "Leg ID cannot be empty.")
        return
    try:
        parameters = (legID, distance, departure, arrival)
        cursor.callproc("add_update_leg", parameters)
        db.commit()
        messagebox.showinfo("Success", "Updated Leg")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error updating leg: {e}")
    finally:
        cursor.close()
    

#8
def stored_procedure_start_route(db, routeID, legID):
    cursor = db.cursor()
    if not routeID:
        messagebox.showerror("Error", "Route ID cannot be empty.")
        return
    try:
        parameters = (routeID, legID)
        cursor.callproc("start_route", parameters)
        db.commit()
        messagebox.showinfo("Success", "Start Route")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error starting route: {e}")
    finally:
        cursor.close()

# 5 Offer Flight
def stored_procedure_offer_flight(db, flightID, routeID, support_airline, support_tail, progress, airplane_status, next_time):
    if not flightID:
        messagebox.showerror("Error", "flightID cannot be empty.")
        return  
    if not routeID:
        messagebox.showerror("Error", "routeID cannot be empty.")
        return  
    try:
        returnFlag = 0
        cursor = db.cursor()
        sql_query = "CALL offer_flight(%s, %s, %s, %s, %s, %s, %s)"
        # query = "call offer_flight('UN_3403', 'westbound_north_milk_run', 'American', 'n380sd', 0, 'on_ground', '15:30:00')"
        parameters = (flightID, routeID, support_airline, support_tail, progress, airplane_status, next_time)
        cursor.execute(sql_query, parameters)
        # cursor.execute(query)
        result = cursor.fetchall()   
        db.commit()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error Offer Flight: {e}")
        returnFlag = 1
    finally:
        if returnFlag == 1:
            return
        messagebox.showinfo("Task Finished", f"Successfully Offer Flight!")
        cursor.close()

# 10 Flight Landing
def stored_procedure_flight_landing(db,flightID):
    if not flightID:
        messagebox.showerror("Error", "flightID cannot be empty.")
        return
    
    plane_state = fetch_plane_state(db, flightID)
    print(plane_state)
    if plane_state is None:
        messagebox.showerror("Error", "No matching flightID found in the database.")
        return
    if plane_state == 'on_ground':
        messagebox.showerror("Error", "The flight has already landed.")
        return
    try:
        cursor = db.cursor()
        sql_query = "Call flight_landing(%s)"
        parameters = (flightID,)
        cursor.execute(sql_query, parameters)
        result = cursor.fetchall()
        db.commit()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error flight landing: {e}")
    finally:
        messagebox.showinfo("Task Finished", f"Successfully land the flight!")
        cursor.close()

# 11 Flight Takeoff
def stored_procedure_flight_takeoff(db,flightID):
    if not flightID:
        messagebox.showerror("Error", "flightID cannot be empty.")
        return
    
    plane_state = fetch_plane_state(db, flightID)
    if plane_state is None:
        messagebox.showerror("Error", "No matching flightID found in the database.")
        return
    if plane_state == 'in_flight':
        messagebox.showerror("Error", "The flight has already token off.")
        return
    try: 
        cursor = db.cursor()
        sql_query = "Call flight_takeoff(%s)"
        parameters = (flightID,)
        cursor.execute(sql_query, parameters)
        result = cursor.fetchall()

        db.commit()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error flight takeoff: {e}")
    finally:
        messagebox.showinfo("Task Finished", f"Successfully takeoff the flight!")
        cursor.close()

# 16 Retire Flight
def stored_procedure_retire_flight(db,flightID):
    if not flightID:
        messagebox.showerror("Error", "flightID cannot be empty.")
        return
    plane_state = fetch_plane_state(db, flightID)
    if plane_state is None:
        messagebox.showerror("Error", "No matching flightID found in the database.")
        return
    if plane_state == 'in_flight':
        messagebox.showerror("Error", "The flight cannot be retired when in air.")
        return   
    try:
        returnFlag = 0
        cursor = db.cursor()
        sql_query = "Call retire_flight(%s)"
        parameters = (flightID,)
        cursor.execute(sql_query, parameters)
        result = cursor.fetchall()
        db.commit()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error flight retire: {e}")
        returnFlag = 1

    finally:
        if returnFlag == 1:
            return
        messagebox.showinfo("Task Finished", f"Successfully retire the flight!")
        cursor.close()        



# 12 Passenger Board
def stored_procedure_passenger_board(db,flightID):
    if not flightID:
        messagebox.showerror("Error", "flightID cannot be empty.")
        return
    
    plane_state = fetch_plane_state(db, flightID)
    if plane_state is None:
        messagebox.showerror("Error", "No matching flightID found in the database.")
        return
    if plane_state == 'in_flight':
        messagebox.showerror("Error", "The flight cannot be boarded when in air.")
        return   
    try:
        returnFlag = 0
        cursor = db.cursor()
        sql_query = "Call passengers_board(%s)"
        parameters = (flightID,)
        cursor.execute(sql_query, parameters)
        result = cursor.fetchall()
        db.commit()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error passenger board: {e}")
        returnFlag = 1
    finally:
        if returnFlag == 1:
            return
        messagebox.showinfo("Task Finished", f"Successfully board passengers!")
        cursor.close()                   

def stored_procedure_grant_pilot_license(db, personID, license):
    try:
        cursor = db.cursor()
        sql_query = "CALL grant_pilot_license(%s, %s)"
        parameters = (personID, license)
        cursor.execute(sql_query, parameters)
        db.commit()
        result = cursor.fetchall()
        db.commit()
        return True  # Operation was successful
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False  # Operation failed

def stored_procedure_assign_pilot (db, flightID, personID):
    try:
        cursor =db.cursor()
        sql_query = "CALL assign_pilot(%s, %s)"
        parameters = (flightID, personID)
        cursor.execute(sql_query, parameters)
        db.commit()
        result = cursor.fetchall()
        db.commit()
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False 
    

def stored_procedure_recycle_crew (db, flightID):
    try:
        cursor =db.cursor()
        sql_query = "CALL recycle_crew(%s)"
        parameters = (flightID,)
        cursor.execute(sql_query, parameters)
        db.commit()
        result = cursor.fetchall()
        db.commit()
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False         

def stored_procedure_remove_pilot_role (db, personID):
    try:
        cursor =db.cursor()
        sql_query = "CALL remove_pilot_role(%s)"
        parameters = (personID,)
        cursor.execute(sql_query, parameters)
        db.commit()
        result = cursor.fetchall()
        db.commit()
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False 

def stored_procedure_passengers_disembark (db, flightID):
    try:
        cursor =db.cursor()
        sql_query = "CALL passengers_disembark(%s)"
        parameters = (flightID,)
        cursor.execute(sql_query, parameters)
        db.commit()
        result = cursor.fetchall()
        db.commit()
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False 

def stored_procedure_remove_passenger_role (db, personID):
    try:
        cursor =db.cursor()
        sql_query = "CALL remove_passenger_role(%s)"
        parameters = (personID,)
        cursor.execute(sql_query, parameters)
        db.commit()
        result = cursor.fetchall()
        db.commit()
        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False 





