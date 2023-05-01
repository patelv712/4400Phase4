import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

from storedViews import *
from simulationCycle import *

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

        button3 = tk.Button(self.button_frame, text="Pilots", width=20, height=2)
        button3.grid(row=1, column=0, padx=10, pady=10)

        button4 = tk.Button(self.button_frame, text="Tickets", width=20, height=2, command=self.tickets)
        button4.grid(row=1, column=1, padx=10, pady=10)

        button5 = tk.Button(self.button_frame, text="People", width=20, height=2)
        button5.grid(row=2, column=0, padx=10, pady=10)

        button6 = tk.Button(self.button_frame, text="Airports", width=20, height=2, command=self.airports)
        button6.grid(row=2, column=1, padx=10, pady=10)

        button7 = tk.Button(self.button_frame, text="Flights", width=20, height=2)
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
