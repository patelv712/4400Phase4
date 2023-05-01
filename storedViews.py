import tkinter as tk
from tkinter import ttk


def display_flights_in_the_air(db):
    # Fetch data from the "flights_in_the_air" view
    cursor = db.cursor()
    cursor.execute("SELECT departing_from, arriving_at, num_flights, flight_list, earliest_arrival, latest_arrival, airplane_list FROM flights_in_the_air")
    flights = cursor.fetchall()

    # Define columns and column names
    columns = ("departing_from", "arriving_at", "num_flights", "flight_list", "earliest_arrival", "latest_arrival", "airplane_list")
    column_names = columns

    # Call show_table function to display the data
    show_table("Flights in the Air", flights, columns, column_names)

def display_flights_on_the_ground(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM flights_on_the_ground;")
    data = cursor.fetchall()
    columns = ("departing_from", "num_flights", "flight_list", "earliest_arrival", "latest_arrival", "airplane_list")
    show_table("Flights on the Ground", data, columns, columns)

def display_people_in_the_air(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM people_in_the_air;")
    data = cursor.fetchall()
    columns = ("departing_from", "arriving_at", "num_airplanes", "airplane_list", "flight_list", "earliest_arrival", "latest_arrival", "num_pilots", "num_passengers", "joint_pilots_passengers", "person_list")
    column_widths = [120, 120, 60, 120, 120, 120, 120, 60, 60, 60, 400]

    show_table("People in the Air", data, columns, columns, column_widths)

def display_people_on_the_ground(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM people_on_the_ground;")
    data = cursor.fetchall()
    columns = ("departing_from", "airport", "airport_name", "city", "state", "num_pilots", "num_passengers", "joint_pilots_passengers", "person_list")
    column_names = columns
    show_table("People on the Ground", data, columns, column_names)

def display_route_summary(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM route_summary;")
    data = cursor.fetchall()
    columns = ("route", "num_legs", "leg_sequence", "route_length", "num_flights", "flight_list", "airport_sequence")
    column_names = columns
    column_widths = [200, 60, 250, 120, 60, 200, 400]

    show_table("Route Summary", data, columns, column_names, column_widths)

def display_alternative_airports(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alternative_airports;")
    data = cursor.fetchall()
    columns = ("city", "state", "num_airports", "airport_code_list", "airport_name_list")
    column_names = columns
    column_widths = [120, 120, 120, 120, 500]  # Increase the width of the airport_name_list column

    show_table("Alternative Airports", data, columns, column_names, column_widths)


# def display_alternative_airports(db):
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM alternative_airports;")
#     data = cursor.fetchall()
#     columns = ("city", "state", "num_airports", "airport_code_list", "airport_name_list")
#     column_names = columns
#
#     show_table("Alternative Airports", data, columns, column_names)


def create_treeview(parent, columns, column_names, column_widths=None):
    treeview = ttk.Treeview(parent, columns=columns, show='headings', height=10)

    if not column_widths:
        column_widths = [120] * len(columns)

    for col, name, width in zip(columns, column_names, column_widths):
        treeview.column(col, anchor=tk.CENTER, width=width)
        treeview.heading(col, text=name)

    treeview.grid(row=0, column=0, sticky=tk.NSEW)
    return treeview

# def create_treeview(parent, columns, column_names):
#     treeview = ttk.Treeview(parent, columns=columns, show='headings', height=10)
#
#     for col, name in zip(columns, column_names):
#         treeview.column(col, anchor=tk.CENTER, width=120)
#         treeview.heading(col, text=name)
#
#     treeview.grid(row=0, column=0, sticky=tk.NSEW)
#     return treeview


def create_scrollbar(parent, treeview):
    scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    return scrollbar


def create_exit_button(parent):
    exit_button = tk.Button(parent, text="Exit", width=5, command=parent.destroy)
    exit_button.grid(row=2, column=0, sticky='s')
    return exit_button


def show_table(title, data, columns, column_names, column_widths=None):
    new_window = tk.Tk()
    new_window.title(title)

    treeview = create_treeview(new_window, columns, column_names, column_widths)
    scrollbar = create_scrollbar(new_window, treeview)
    exit_button = create_exit_button(new_window)

    for line in data:
        treeview.insert("", tk.END, values=line)

    new_window.mainloop()


# def show_table(title, data, columns, column_names):
#     new_window = tk.Tk()
#     new_window.title(title)
#
#     treeview = create_treeview(new_window, columns, column_names)
#     scrollbar = create_scrollbar(new_window, treeview)
#     exit_button = create_exit_button(new_window)
#
#     for line in data:
#         treeview.insert("", tk.END, values=line)
#
#     new_window.mainloop()

