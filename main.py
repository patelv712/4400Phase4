import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURMYSQLPASSWORD",
        database="employee_db"
    )
    return conn

# Main window
root = tk.Tk()
root.title("Airlane System")

# Start main loop
root.mainloop()