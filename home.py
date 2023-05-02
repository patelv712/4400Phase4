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

        button3 = tk.Button(self.button_frame, text="Add Routes and Legs", width=20, height=2)
        button3.grid(row=1, column=0, padx=10, pady=10)

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

        button1 = tk.Button(self.button_frame, text="Grant Pilot License", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Remove Pilot", width=20, height=2)
        button2.grid(row=0, column=1, padx=10, pady=10)        

        # button2 = tk.Button(self.button_frame, text="Show Pilots", width=20, height=2, command=lambda: display_pilots(self.db))
        # button2.grid(row=0, column=1, padx=10, pady=10)

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

        button1 = tk.Button(self.button_frame, text="Add People", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text = "Passengers Board", width=20, height=2, command = self.passenger_board)
        button2.grid(row=0, column=1, padx=10, pady=10)

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
