import tkinter as tk
from tkinter import messagebox
import mysql.connector
from home import *

def main():

    db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="liululu0201",
            database="flight_management"
        )
    home(db)
    db.close()

if __name__ == "__main__":
    main()
