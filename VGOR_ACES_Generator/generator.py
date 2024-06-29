import pandas as pd 
import tkinter as tk
from tkinter import filedialog, messagebox

# Create a Frame for the GUI
gui = tk.Tk()
gui.title('ACES Generator')
gui.geometry('500x500')

# Function to generate the Jobber Path
def load_jobber_file():
    jobber_path.set(filedialog.askopenfilename())

# Function to generate the ACES Data File Path
def load_aces_data_file():
    aces_data_path.set(filedialog.askopenfilename())

# Function to generate the Output (ACES) Path
def gen_output_path():
    output_path.set(filedialog.asksaveasfilename(defaultextension=".xlsx"))

# Variables to store the file paths
jobber_path = tk.StringVar()
aces_data_path = tk.StringVar()
output_path = tk.StringVar()

# Introduction for the GUI
greeting = tk.Label(text="Welcome to the ACES Generator", font=("Agency FB", 22))
greeting.grid()

# File Selection Section
## Jobber Section 
tk.Label(gui, text="Jobber File:", font=("Agency FB", 14)).grid(row=1, column=0, pady=2)
tk.Entry(gui, textvariable=jobber_path, width=40).grid(row=1, column=1, padx=10, pady=5)
tk.Button(gui, text="Browse", command=load_jobber_file).grid(row=1, column=2, padx=10, pady=5)
## ACES Data File Section
tk.Label(gui, text="ACES Data File:", font=("Agency FB", 14)).grid(row=2, column=0, pady=2)
tk.Entry(gui, textvariable=aces_data_path, width=40).grid(row=2, column=1, padx=10, pady=5)
tk.Button(gui, text="Browse", command=load_aces_data_file).grid(row=2, column=2, padx=10, pady=5)
## Output File Section
tk.Label(gui, text="Output File Path:", font=("Agency FB", 14)).grid(row=3, column=0, pady=2)
tk.Entry(gui, textvariable=output_path, width=40).grid(row=3, column=1, padx=10, pady=5)
tk.Button(gui, text="Save As", command=gen_output_path).grid(row=3, column=2, padx=10, pady=5)


gui.mainloop()