import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

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
        button1 = tk.Button(self.button_frame, text="Airplanes", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="Routes & Legs", width=20, height=2)
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = tk.Button(self.button_frame, text="Pilots", width=20, height=2)
        button3.grid(row=1, column=0, padx=10, pady=10)

        button4 = tk.Button(self.button_frame, text="Tickets", width=20, height=2)
        button4.grid(row=1, column=1, padx=10, pady=10)

        button5 = tk.Button(self.button_frame, text="People", width=20, height=2)
        button5.grid(row=2, column=0, padx=10, pady=10)

        button6 = tk.Button(self.button_frame, text="Airports", width=20, height=2)
        button6.grid(row=2, column=1, padx=10, pady=10)

        button7 = tk.Button(self.button_frame, text="Flights", width=20, height=2)
        button7.grid(row=3, column=0, padx=10, pady=10)

        button8 = tk.Button(self.button_frame, text="Views and Simulation Cycle", width=20, height=2, command=self.views)
        button8.grid(row=3, column=1, padx=10, pady=10)

        button9 = tk.Button(self.button_frame, text="Tables", width=20, height=2)
        button9.grid(row=4, column=0, padx=10, pady=10)

        button10 = tk.Button(self.button_frame, text="Button 10", width=20, height=2)
        button10.grid(row=4, column=1, padx=10, pady=10)

        self.mainpage.mainloop()




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


        button1 = tk.Button(self.button_frame, text="V1 Flights in the air", width=20, height=2)
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = tk.Button(self.button_frame, text="V2 Flights on the ground", width=20, height=2)
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = tk.Button(self.button_frame, text="V3 People in the air", width=20, height=2)
        button3.grid(row=1, column=0, padx=10, pady=10)

        button4 = tk.Button(self.button_frame, text="V4 People on the ground", width=20, height=2)
        button4.grid(row=1, column=1, padx=10, pady=10)

        button5 = tk.Button(self.button_frame, text="V5 Route Summary", width=20, height=2)
        button5.grid(row=2, column=0, padx=10, pady=10)

        button6 = tk.Button(self.button_frame, text="V6 Alternative airports", width=20, height=2)
        button6.grid(row=2, column=1, padx=10, pady=10)

        button7 = tk.Button(self.button_frame, text="Simulation Recycle", width=20, height=2)
        button7.grid(row=3, column=0, padx=10, pady=10)
