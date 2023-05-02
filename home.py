import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

from storedViews import *
from simulationCycle import *
from storedProcedures import *

class home:

    def __init__(self, db):
        self.db = db
        self.mainpage()

    '''
        main page
    '''

    def mainpage(self):
        self.mainpage = tk.Tk()
        self.mainpage.title("Flight Management System")
        self.mainpage.geometry("800x600")

        self.mainpage_label = tk.Label(self.mainpage, text="Flight Management System", font=("Arial", 20))
        self.mainpage_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.mainpage)
        self.button_frame.pack(pady=10)

        # Create the buttons with larger width and height and add them to the grid in a row-wise order
        button1 = tk.Button(self.button_frame, text="Airplanes", width=20, height=2, command=self.airplanes)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Routes & Legs", width=20, height=2, command=self.routes)
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = tk.Button(self.button_frame, text="Pilots", width=20, height=2, command=self.pilots)
        button3.grid(row=1, column=0, padx=10, pady=10)

        button4 = tk.Button(self.button_frame, text="Tickets", width=20, height=2, command=self.tickets)
        button4.grid(row=1, column=1, padx=10, pady=10)

        button5 = tk.Button(self.button_frame, text="People", width=20, height=2, command=self.people)
        button5.grid(row=2, column=0, padx=10, pady=10)

        button6 = tk.Button(self.button_frame, text="Airports", width=20, height=2, command=self.airports)
        button6.grid(row=2, column=1, padx=10, pady=10)

        button7 = tk.Button(self.button_frame, text="Flights", width=20, height=2, command=self.flights)
        button7.grid(row=3, column=0, padx=10, pady=10)

        button8 = tk.Button(self.button_frame, text="Views and Simulation Cycle", width=20, height=2, command=self.views)
        button8.grid(row=3, column=1, padx=10, pady=10)

        button9 = tk.Button(self.button_frame, text="Tables", width=20, height=2)
        button9.grid(row=4, column=0, padx=10, pady=10)

        self.mainpage.mainloop()



    '''
        airplane
    '''
    def airplanes(self):
        self.airplanes = tk.Tk()
        self.airplanes.title("Airplanes")
        self.airplanes.geometry("800x600")

        self.views_label = tk.Label(self.airplanes, text="Airplanes", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.airplanes)
        self.button_frame.pack(pady=10)


        button1 = tk.Button(self.button_frame, text="Add Airplane", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)
    '''
        airports
    '''
    def airports(self):
        self.airports = tk.Tk()
        self.airports.title("Airports")
        self.airports.geometry("800x600")

        self.views_label = tk.Label(self.airports, text="Airports", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.airports)
        self.button_frame.pack(pady=10)


        button1 = tk.Button(self.button_frame, text="Add Airport", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

    '''
        tickets
    '''
    def tickets(self):
        self.tickets = tk.Tk()
        self.tickets.title("Tickets")
        self.tickets.geometry("800x600")

        self.views_label = tk.Label(self.tickets, text="Tickets", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.tickets)
        self.button_frame.pack(pady=10)

        button1 = tk.Button(self.button_frame, text="Add Tickets", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

    '''
        Routes & Legs
    '''



    def routes(self):
        self.routes = tk.Tk()
        self.routes.title("Routes & Legs")
        self.routes.geometry("800x600")

        self.views_label = tk.Label(self.routes, text="Routes & Legs", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.routes)
        self.button_frame.pack(pady=10)


        button1 = tk.Button(self.button_frame, text="Add Route", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Add Legs", width=20, height=2)
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = tk.Button(self.button_frame, text="Extend Route", width=20, height=2, command=self.open_extend_route_page)
        button3.grid(row=1, column=0, padx=10, pady=10)

    '''
           Query 9 Extend Route
    '''
    def open_extend_route_page(self):
        self.extend_route_window = tk.Toplevel()
        self.extend_route_window.title("Extend Route")

        # Create labels and input fields
        route_id_label = tk.Label(self.extend_route_window, text="Route ID:")
        route_id_entry = tk.Entry(self.extend_route_window)
        route_id_label.grid(row=0, column=0, padx=5, pady=5)
        route_id_entry.grid(row=0, column=1, padx=5, pady=5)

        leg_id_label = tk.Label(self.extend_route_window, text="Leg ID:")
        leg_id_dropdown = ttk.Combobox(self.extend_route_window)
        leg_id_label.grid(row=1, column=0, padx=5, pady=5)
        leg_id_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Populate the dropdown with legIDs from the database
        leg_ids = self.get_leg_ids()
        leg_id_dropdown['values'] = leg_ids

        # Create buttons
        submit_button = tk.Button(self.extend_route_window, text="Submit",
                                  command=lambda: self.extend_route(route_id_entry.get(), leg_id_dropdown.get()))
        cancel_button = tk.Button(self.extend_route_window, text="Cancel", command=self.extend_route_window.destroy)
        submit_button.grid(row=2, column=0, padx=5, pady=5)
        cancel_button.grid(row=2, column=1, padx=5, pady=5)

    def get_leg_ids(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT legID FROM leg;")
        leg_ids = [row[0] for row in cursor.fetchall()]
        return leg_ids

    def extend_route(self, route_id, leg_id):
        cursor = self.db.cursor()
        try:
            cursor.callproc("extend_route", [route_id, leg_id])
            self.db.commit()
            messagebox.showinfo("Success", "Route extended successfully.")
            self.extend_route_window.destroy()
        except Exception as e:
            self.db.rollback()
            messagebox.showerror("Error", f"Error extending route: {e}")

    '''
        pilots
    '''
    def pilots(self):
        self.pilots = tk.Tk()
        self.pilots.title("Pilots")
        self.pilots.geometry("800x600")

        self.views_label = tk.Label(self.pilots, text="Pilots", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.pilots)
        self.button_frame.pack(pady=10)

        button1 = tk.Button(self.button_frame, text="Grant Pilot License", width=20, height=2, command=self.Grant_Pilot_License)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Assign Pilot", width=20, height=2, command=self.Assign_Pilot)
        button2.grid(row=0, column=1, padx=10, pady=10) 

        button3 = tk.Button(self.button_frame, text="Recycle Crew", width=20, height=2, command=self.Recycle_Crew)
        button3.grid(row=1, column=0, padx=10, pady=10)     

        button4 = tk.Button(self.button_frame, text="Remove Pilot Role", width=20, height=2, command=self.Remove_Pilot_Role)
        button4.grid(row=1, column=1, padx=10, pady=10)   

    '''
        people
    '''
    def people(self):
        self.people = tk.Tk()
        self.people.title("People")
        self.people.geometry("800x600")

        self.views_label = tk.Label(self.people, text="People", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.people)
        self.button_frame.pack(pady=10)

        button1 = tk.Button(self.button_frame, text="Add People", width=20, height=2, command=self.open_add_people_page)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text = "Passengers Board", width=20, height=2, command = self.passenger_board)
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = tk.Button(self.button_frame, text = "Passengers Disembark", width=20, height=2, command = self.Passenger_Disembark)
        button3.grid(row=1, column=0, padx=10, pady=10)

        button4 = tk.Button(self.button_frame, text = "Remove Passengers Role", width=20, height=2, command = self.Remove_Passenger_Role)
        button4.grid(row=1, column=1, padx=10, pady=10)

    '''
            add person
    '''

    def open_add_people_page(self):
        add_people_page = tk.Toplevel(self.mainpage)
        add_people_page.title("Add People")
        add_people_page.geometry("400x300")

        tk.Label(add_people_page, text="Person ID:").grid(row=0, column=0, sticky="e")
        person_id_entry = tk.Entry(add_people_page)
        person_id_entry.grid(row=0, column=1)

        tk.Label(add_people_page, text="First Name:").grid(row=1, column=0, sticky="e")
        first_name_entry = tk.Entry(add_people_page)
        first_name_entry.grid(row=1, column=1)

        tk.Label(add_people_page, text="Last Name:").grid(row=2, column=0, sticky="e")
        last_name_entry = tk.Entry(add_people_page)
        last_name_entry.grid(row=2, column=1)

        tk.Label(add_people_page, text="Location ID:").grid(row=3, column=0, sticky="e")
        location_id_entry = tk.Entry(add_people_page)
        location_id_entry.grid(row=3, column=1)

        tk.Label(add_people_page, text="Tax ID:").grid(row=4, column=0, sticky="e")
        tax_id_entry = tk.Entry(add_people_page)
        tax_id_entry.grid(row=4, column=1)

        tk.Label(add_people_page, text="Experience:").grid(row=5, column=0, sticky="e")
        experience_entry = tk.Entry(add_people_page)
        experience_entry.grid(row=5, column=1)

        tk.Label(add_people_page, text="Flying Airline:").grid(row=6, column=0, sticky="e")
        flying_airline_entry = tk.Entry(add_people_page)
        flying_airline_entry.grid(row=6, column=1)

        tk.Label(add_people_page, text="Flying Tail:").grid(row=7, column=0, sticky="e")
        flying_tail_entry = tk.Entry(add_people_page)
        flying_tail_entry.grid(row=7, column=1)

        tk.Label(add_people_page, text="Miles:").grid(row=8, column=0, sticky="e")
        miles_entry = tk.Entry(add_people_page)
        miles_entry.grid(row=8, column=1)

        submit_button = tk.Button(add_people_page, text="Submit",
                                  command=lambda: self.add_person_to_db(add_people_page, person_id_entry,
                                                                        first_name_entry, last_name_entry,
                                                                        location_id_entry, tax_id_entry,
                                                                        experience_entry, flying_airline_entry,
                                                                        flying_tail_entry, miles_entry))
        submit_button.grid(row=9, column=0, columnspan=2)

    def add_person_to_db(self, add_people_page, person_id_entry, first_name_entry, last_name_entry, location_id_entry,
                         tax_id_entry, experience_entry, flying_airline_entry, flying_tail_entry, miles_entry):
        person_id = person_id_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        location_id = location_id_entry.get()
        tax_id = tax_id_entry.get()
        experience = int(experience_entry.get()) if experience_entry.get() else None
        flying_airline = flying_airline_entry.get()
        flying_tail = flying_tail_entry.get()
        miles = int(miles_entry.get()) if miles_entry.get() else None

        cursor = self.db.cursor()

        try:
            cursor.callproc("add_person",
                            [person_id, first_name, last_name, location_id, tax_id, experience, flying_airline,
                             flying_tail, miles])
            self.db.commit()
            messagebox.showinfo("Success", "Person added successfully!")
            add_people_page.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error adding person: {e}")
        finally:
            cursor.close()

    def passenger_board(self):
        self.passenger_board = tk.Tk()
        self.passenger_board.title ("Passenger_board")
        self.passenger_board.geometry("500x250")

        flightID = fetch_flightID (self.db)
        sorted_flightID = sorted(flightID)
        label_flightID = tk.Label(self.passenger_board, text = "flightID: ", bg="light grey")
        label_flightID.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        dropdown_flightID = ttk.Combobox (self.passenger_board, values = sorted_flightID)
        dropdown_flightID.grid (row=0,column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.passenger_board, text="Cancel", command=self.passenger_board.destroy)
        cancel_button.grid(row=4,column=0, columnspan=2,pady=100)
        continue_button = tk.Button(self.passenger_board, text="Continue", command=lambda: 
                                  stored_procedure_passenger_board(self.db,dropdown_flightID.get()))
        continue_button.grid(row=4, column=2, columnspan=2, pady=100)

    '''
        passenger disembark
    '''
    def Passenger_Disembark(self):
        self.Passenger_Disembark = tk.Tk()
        self.Passenger_Disembark.title ("Passenger Disembark")
        self.Passenger_Disembark.geometry("700x400")    

        flightID = fetch_flightID (self.db)
        sorted_flightID = sorted(flightID)
        label_flightID = tk.Label(self.Passenger_Disembark, text="flightID")
        label_flightID.grid(row=0,column=0,padx=5,pady=5)
        dropdown_flightID = ttk.Combobox (self.Passenger_Disembark, values = sorted_flightID)
        dropdown_flightID.grid (row=0,column=1, padx=5, pady=5)  

        cancel_button = tk.Button(self.Passenger_Disembark, text="Cancel", command=self.Passenger_Disembark.destroy)
        cancel_button.grid(row=2,column=0, columnspan=2,pady=10)
        recycle_crew_button = tk.Button(self.Passenger_Disembark, text="continue", command=lambda: 
                                  stored_procedure_passengers_disembark (self.db,
                                  dropdown_flightID.get()))
        recycle_crew_button.grid(row=2, column=3, columnspan=2, pady=10)
     
    '''
        remove passenger role
    '''
    def Remove_Passenger_Role(self):
        self.Remove_Passenger_Role = tk.Tk()
        self.Remove_Passenger_Role.title ("Remove Pilot Role")
        self.Remove_Passenger_Role.geometry("700x400")    

        personID = fetch_personID (self.db)
        sorted_personID = sorted(personID)
        label_personID = tk.Label(self.Remove_Passenger_Role, text="personID")
        label_personID.grid(row=0,column=0,padx=5,pady=5)
        dropdown_personID = ttk.Combobox (self.Remove_Passenger_Role, values = sorted_personID)
        dropdown_personID.grid (row=0,column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.Remove_Passenger_Role, text="Cancel", command=self.Remove_Passenger_Role.destroy)
        cancel_button.grid(row=2,column=0, columnspan=2,pady=10)
        remove_passenger_button = tk.Button(self.Remove_Passenger_Role, text="Remove Passenger", command=lambda: 
                                  stored_procedure_remove_passenger_role (self.db,
                                  dropdown_personID.get()))
        remove_passenger_button.grid(row=2, column=3, columnspan=2, pady=10)
    '''
        grant pilots license
    '''
    def Grant_Pilot_License(self):
        self.Grant_Pilot_License = tk.Tk()
        self.Grant_Pilot_License.title ("Grant Pilot License")
        self.Grant_Pilot_License.geometry("700x400")    

        personID = fetch_personID (self.db)
        sorted_personID = sorted(personID)
        label_personID = tk.Label(self.Grant_Pilot_License, text="personID")
        label_personID.grid(row=0,column=0,padx=5,pady=5)
        dropdown_personID = ttk.Combobox (self.Grant_Pilot_License, values = sorted_personID)
        dropdown_personID.grid (row=0,column=1, padx=5, pady=5)

        license_type = fetch_license_type (self.db)
        sorted_license_type = sorted(license_type)
        label_license_type = tk.Label(self.Grant_Pilot_License, text="License type")
        label_license_type.grid(row=1,column=0,padx=5,pady=5)
        dropdown_license_type = ttk.Combobox (self.Grant_Pilot_License, values = sorted_license_type)
        dropdown_license_type.grid (row=1,column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.Grant_Pilot_License, text="Cancel", command=self.Grant_Pilot_License.destroy)
        cancel_button.grid(row=2,column=0, columnspan=2,pady=10)
        grant_button = tk.Button(self.Grant_Pilot_License, text="Grant", command=lambda: 
                                  stored_procedure_grant_pilot_license (self.db,
                                  dropdown_personID.get(),
                                  dropdown_license_type.get()))
        grant_button.grid(row=2, column=3, columnspan=2, pady=10)        
    '''
        assign pilot
    '''
    def Assign_Pilot(self):
        self.Assign_Pilot = tk.Tk()
        self.Assign_Pilot.title ("Grant Pilot License")
        self.Assign_Pilot.geometry("700x400")    
  

        personID = fetch_personID (self.db)
        sorted_personID = sorted(personID)
        label_personID = tk.Label(self.Assign_Pilot, text="personID")
        label_personID.grid(row=0,column=0,padx=5,pady=5)
        dropdown_personID = ttk.Combobox (self.Assign_Pilot, values = sorted_personID)
        dropdown_personID.grid (row=0,column=1, padx=5, pady=5)

        flightID = fetch_flightID (self.db)
        sorted_flightID = sorted(flightID)
        label_flightID = tk.Label(self.Assign_Pilot, text="Flight")
        label_flightID.grid(row=1,column=0,padx=5,pady=5)
        dropdown_flightID = ttk.Combobox (self.Assign_Pilot, values = sorted_flightID)
        dropdown_flightID.grid (row=1,column=1, padx=5, pady=5)      

        cancel_button = tk.Button(self.Assign_Pilot, text="Cancel", command=self.Assign_Pilot.destroy)
        cancel_button.grid(row=2,column=0, columnspan=2,pady=10)
        assign_button = tk.Button(self.Assign_Pilot, text="Assign", command=lambda: 
                                  stored_procedure_assign_pilot (self.db,
                                  dropdown_personID.get(),
                                  dropdown_flightID.get()))
        assign_button.grid(row=2, column=3, columnspan=2, pady=10)   
    '''
        recycle crew
    '''
    def Recycle_Crew(self):
        self.Recycle_Crew = tk.Tk()
        self.Recycle_Crew.title ("Recycle Crew")
        self.Recycle_Crew.geometry("700x400")    

        flightID = fetch_flightID (self.db)
        sorted_flightID = sorted(flightID)
        label_flightID = tk.Label(self.Recycle_Crew, text="Flight")
        label_flightID.grid(row=0,column=0,padx=5,pady=5)
        dropdown_flightID = ttk.Combobox (self.Recycle_Crew, values = sorted_flightID)
        dropdown_flightID.grid (row=0,column=1, padx=5, pady=5)  

        cancel_button = tk.Button(self.Recycle_Crew, text="Cancel", command=self.Recycle_Crew.destroy)
        cancel_button.grid(row=2,column=0, columnspan=2,pady=10)
        recycle_crew_button = tk.Button(self.Recycle_Crew, text="Recycle Crew", command=lambda: 
                                  stored_procedure_recycle_crew (self.db,
                                  dropdown_flightID.get()))
        recycle_crew_button.grid(row=2, column=3, columnspan=2, pady=10)

    '''
        remove pilot role
    '''
    def Remove_Pilot_Role(self):
        self.Remove_Pilot_Role = tk.Tk()
        self.Remove_Pilot_Role.title ("Remove Pilot Role")
        self.Remove_Pilot_Role.geometry("700x400")    

        personID = fetch_personID (self.db)
        sorted_personID = sorted(personID)
        label_personID = tk.Label(self.Remove_Pilot_Role, text="personID")
        label_personID.grid(row=0,column=0,padx=5,pady=5)
        dropdown_personID = ttk.Combobox (self.Remove_Pilot_Role, values = sorted_personID)
        dropdown_personID.grid (row=0,column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.Remove_Pilot_Role, text="Cancel", command=self.Remove_Pilot_Role.destroy)
        cancel_button.grid(row=2,column=0, columnspan=2,pady=10)
        remove_pilot_button = tk.Button(self.Remove_Pilot_Role, text="Remove Pilot", command=lambda: 
                                  stored_procedure_remove_pilot_role (self.db,
                                  dropdown_personID.get()))
        remove_pilot_button.grid(row=2, column=3, columnspan=2, pady=10)

    '''
        flights
    '''
    def flights(self):
        self.flights = tk.Tk()
        self.flights.title("Flights")
        self.flights.geometry("800x600")

        self.views_label = tk.Label(self.flights, text="Flights", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.flights)
        self.button_frame.pack(pady=10)

        button1 = tk.Button(self.button_frame, text="Offer Flight", width=20, height=2, command = self.Offer_Flight)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Flight Landing", width=20, height=2, command = self.flight_landing)
        button2.grid(row=0, column=1, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Flight Takeoff", width=20, height=2, command = self.flight_takeoff)
        button2.grid(row=1, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Retire Flight", width=20, height=2, command = self.retire_flight)
        button2.grid(row=1, column=1, padx=10, pady=10)



    # stored procedure 5#
    def Offer_Flight(self):
        self.Offer_Flight = tk.Tk()
        self.Offer_Flight.title ("Offer Flight")
        self.Offer_Flight.geometry("700x400")

        label_flightID = tk.Label(self.Offer_Flight, text = "FlightID: ")
        label_flightID.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        entry_flightID = tk.Entry(self.Offer_Flight)
        entry_flightID.grid (row=0, column=1, padx=5, pady=5)

        label_routeID = tk.Label(self.Offer_Flight, text="routeID: ")
        label_routeID.grid(row = 1, column= 0, padx=5, pady=5, sticky="e")
        entry_routeID = tk.Entry(self.Offer_Flight)
        entry_routeID.grid (row=1, column=1, padx=5, pady=5)

        label_support_tail = tk.Label(self.Offer_Flight, text="support_tail: ")
        label_support_tail.grid(row = 0, column=2, padx=20, pady=5, sticky="e")
        entry_support_tail = tk.Entry(self.Offer_Flight)
        entry_support_tail.grid (row=0, column=3, padx=5, pady=5)

        label_progress = tk.Label(self.Offer_Flight, text="progress: ")
        label_progress.grid(row=1, column=2, padx=20, pady=5, sticky="e")
        entry_progress = tk.Entry(self.Offer_Flight)
        entry_progress.grid (row=1, column=3, padx=5, pady=5)

        label_next_time = tk.Label (self.Offer_Flight, text="next_time: ")
        label_next_time.grid (row=3,column=2, padx=5, pady=5, sticky = "e")
        entry_next_time = tk.Entry (self.Offer_Flight)
        entry_next_time.grid (row=3,column=3, padx=5,pady=5)

        support_airlineID = fetch_airlineID (self.db)
        sorted_support_airline = sorted(support_airlineID)
        label_support_airline = tk.Label(self.Offer_Flight, text="support_airline")
        label_support_airline.grid(row=2,column=0,padx=5,pady=5)
        dropdown_support_airline = ttk.Combobox (self.Offer_Flight, values = sorted_support_airline)
        dropdown_support_airline.grid (row=2,column=1, padx=5, pady=5)

        sorted_airplane_status = ["on_ground", "in_flight"]
        label_airplane_status = tk.Label(self.Offer_Flight, text="airplane_status")
        label_airplane_status.grid(row=2,column=2,padx=5,pady=5)
        dropdown_airplane_status = ttk.Combobox (self.Offer_Flight, values = sorted_airplane_status)
        dropdown_airplane_status.grid (row=2,column=3, padx=5, pady=5)

        cancel_button = tk.Button(self.Offer_Flight, text="Cancel", command=self.Offer_Flight.destroy)
        cancel_button.grid(row=4,column=0, columnspan=2,pady=10)
        submit_button = tk.Button(self.Offer_Flight, text="Submit", command=lambda: 
                                  stored_procedure_offer_flight (self.db,
                                                entry_flightID.get(),
                                                entry_routeID.get(), 
                                                dropdown_support_airline.get(),
                                                entry_support_tail.get(), 
                                                entry_progress.get(),
                                                dropdown_airplane_status.get(),
                                                entry_next_time.get()))
        submit_button.grid(row=4, column=2, columnspan=2, pady=10)
    
    def flight_landing(self):
        self.flight_landing = tk.Tk()
        self.flight_landing.title ("Flight_Landing")
        self.flight_landing.geometry("600x300")

        label_flightID = tk.Label(self.flight_landing, text = "flightID: ", bg="light grey")
        label_flightID.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        entry_flightID = tk.Entry(self.flight_landing)
        entry_flightID.grid (row=0, column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.flight_landing, text="Cancel", command=self.flight_landing.destroy)
        cancel_button.grid(row=4,column=0, columnspan=2,pady=100)
        submit_button = tk.Button(self.flight_landing, text="Update", command=lambda: 
                                  stored_procedure_flight_landing(self.db, entry_flightID.get()))
        submit_button.grid(row=4, column=2, columnspan=2, pady=100)

    def flight_takeoff(self):
        self.flight_takeoff = tk.Tk()
        self.flight_takeoff.title ("Flight_Takeoff")
        self.flight_takeoff.geometry("500x250")

        label_flightID = tk.Label(self.flight_takeoff, text = "flightID: ", bg="light grey")
        label_flightID.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        entry_flightID = tk.Entry(self.flight_takeoff)
        entry_flightID.grid (row=0, column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.flight_takeoff, text="Cancel", command=self.flight_takeoff.destroy)
        cancel_button.grid(row=4,column=0, columnspan=2,pady=100)
        submit_button = tk.Button(self.flight_takeoff, text="Update", command=lambda: 
                                  stored_procedure_flight_takeoff(self.db,entry_flightID.get()))
        submit_button.grid(row=4, column=2, columnspan=2, pady=100)

    def retire_flight(self):
        self.retire_flight = tk.Tk()
        self.retire_flight.title ("Retire_Flight")
        self.retire_flight.geometry("500x250")

        label_flightID = tk.Label(self.retire_flight, text = "flightID: ", bg="light grey")
        label_flightID.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        entry_flightID = tk.Entry(self.retire_flight)
        entry_flightID.grid (row=0, column=1, padx=5, pady=5)

        cancel_button = tk.Button(self.retire_flight, text="Cancel", command=self.retire_flight.destroy)
        cancel_button.grid(row=4,column=0, columnspan=2,pady=100)
        submit_button = tk.Button(self.retire_flight, text="Update", command=lambda: 
                                  stored_procedure_retire_flight(self.db,entry_flightID.get()))
        submit_button.grid(row=4, column=2, columnspan=2, pady=100)
    '''
        views
    '''
    def views(self):
        self.views = tk.Tk()
        self.views.title("Views and Simulation Cycle")
        self.views.geometry("800x600")

        self.views_label = tk.Label(self.views, text="Views and Simulation Cycle", font=("Arial", 20))
        self.views_label.pack(pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.views)
        self.button_frame.pack(pady=10)


        button1 = tk.Button(self.button_frame, text="V1 Flights in the air", width=20, height=2, command=lambda: display_flights_in_the_air(self.db))
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="V2 Flights on the ground", width=20, height=2, command=lambda: display_flights_on_the_ground(self.db))
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = tk.Button(self.button_frame, text="V3 People in the air", width=20, height=2, command=lambda: display_people_in_the_air(self.db))
        button3.grid(row=1, column=0, padx=10, pady=10)

        button4 = tk.Button(self.button_frame, text="V4 People on the ground", width=20, height=2, command=lambda: display_people_on_the_ground(self.db))
        button4.grid(row=1, column=1, padx=10, pady=10)

        button5 = tk.Button(self.button_frame, text="V5 Route Summary", width=20, height=2, command=lambda: display_route_summary(self.db))
        button5.grid(row=2, column=0, padx=10, pady=10)

        button6 = tk.Button(self.button_frame, text="V6 Alternative airports", width=20, height=2, command=lambda: display_alternative_airports(self.db))
        button6.grid(row=2, column=1, padx=10, pady=10)

        button7 = tk.Button(self.button_frame, text="Simulation Recycle", width=20, height=2, command=lambda: simulation_cycle_window(self.db))
        button7.grid(row=3, column=0, padx=10, pady=10)
