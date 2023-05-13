import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def simulation_cycle_window(db):
    new_window = tk.Tk()
    new_window.title("Simulation Cycle")
    new_window.geometry("400x300")

    label = tk.Label(new_window, text="Simulation Cycle")
    label.pack(pady=10)

    def run_simulation_cycle():
        cursor = db.cursor()
        cursor.callproc("simulation_cycle")
        db.commit()
        messagebox.showinfo("Success", "Simulation cycle executed successfully")
        new_window.destroy()

    run_button = tk.Button(new_window, text="Run", command=run_simulation_cycle)
    run_button.pack(pady=10)

    cancel_button = tk.Button(new_window, text="Cancel", command=new_window.destroy)
    cancel_button.pack(pady=10)

    new_window.mainloop()

