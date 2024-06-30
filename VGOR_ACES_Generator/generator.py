import pandas as pd 
import tkinter as tk
from tkinter import filedialog, messagebox

# Create a Frame for the GUI
gui = tk.Tk()
gui.iconbitmap("VGOR_ACES_Generator\logo.ico")
gui.title('ACES Generator')
gui.geometry('810x550')
gui.resizable(False,False)

# Variables to store the file paths
jobber_path = tk.StringVar()
aces_data_path = tk.StringVar()
output_path = tk.StringVar()

# Function to generate the Jobber Path
def load_jobber_file():
    jobber_path.set(filedialog.askopenfilename())

# Function to generate the ACES Data File Path
def load_aces_data_file():
    aces_data_path.set(filedialog.askopenfilename())

# Function to generate the Output (ACES) Path
def gen_output_path():
    output_path.set(filedialog.asksaveasfilename(defaultextension=".xlsx"))

# Generate DataFrame for the Output File following ACES Guideline
def output_dataframe():
    columns = ["Part Number","Brand ID","Part Type","Part Type Description","Year","Make","Model","Submodel","Region"]
    output_df = pd.DataFrame(columns=columns)
    if output_path.get():
        output_df.to_excel(output_path.get())
        messagebox.showinfo("Success", "Output File Generated Successfully!")
    else:
        messagebox.showerror("Error", "Please specify a valid output path.")

# Introduction for the GUI
greeting = tk.Label(text="ACES Generator v1.0", font=("Agency FB", 30))
greeting.grid(row=0 , column=0, pady=10, columnspan=3)

# Description on how to use the ACES Generator
description_text = """
This is a tool used to generate ACES Data that you can use to copy and paste onto the Expanded Smart Sheet that SEMA DATA provides.
1st Step -> Upload Current Jobber into the Jobber Selection. Usually its called (VGOR_Jobber_Month_Year)
2nd Step -> Upload ACES Part Type and YMMSR workbook into ACES Data File. Create one through copying Expanded Smart Sheets.
3rd Step -> Create a Output File for the Generated ACES Data.
4th Step -> Click Generate ACES and then with the ACES Data , copy and paste into Expanded Smart Sheet
5th Step -> Click finish when done. 
Created by: Edmond Wu (ed.dev.1226@gmail.com)
"""
description = tk.Label(text=description_text, justify="left" ,font=("Agency FB", 14))
description.grid(row=1 , column=0, pady=10, padx=10, columnspan=3)

# File Selection Section
## Jobber Section 
tk.Label(gui, text="Jobber File:", font=("Agency FB", 24)).grid(row=2, column=0, pady=2)
tk.Entry(gui, textvariable=jobber_path, width=40).grid(row=2, column=1, padx=10, pady=5)
tk.Button(gui, text="Browse", command=load_jobber_file).grid(row=2, column=2, padx=10, pady=5)
## ACES Data File Section
tk.Label(gui, text="ACES Data File:", font=("Agency FB", 24)).grid(row=3, column=0, pady=2)
tk.Entry(gui, textvariable=aces_data_path, width=40).grid(row=3, column=1, padx=10, pady=5)
tk.Button(gui, text="Browse", command=load_aces_data_file).grid(row=3, column=2, padx=10, pady=5)
## Output File Sections
tk.Label(gui, text="Output File Path:", font=("Agency FB", 24)).grid(row=4, column=0, padx=10, pady=2)
tk.Entry(gui, textvariable=output_path, width=40).grid(row=4, column=1, padx=10, pady=5)
tk.Button(gui, text="Save As", command=gen_output_path).grid(row=4, column=2, padx=10, pady=5)


# Buttons Section (Generate ACES Button and Exit Button)
tk.Button(gui, text="Generate ACES", command=output_dataframe).grid(row=5, column=1, padx=10, pady=5)
tk.Button(gui, text="Exit", command=gui.quit).grid(row=5, column=2, padx=10, pady=5)


gui.mainloop()