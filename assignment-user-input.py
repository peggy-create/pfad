# -*- coding: utf-8 -*-

import tkinter as tk  # Import tkinter library for GUI creation
from tkinter import messagebox  # Import messagebox from tkinter for displaying message boxes

# Create main window instance
mainWindow = tk.Tk()
mainWindow.title("BMI Calculator")  # Set window title
mainWindow.geometry("400x300")  # Set window size

# Define function to calculate BMI
def calculateBmi():
    name = entryName.get()  # Get name input
    age = entryAge.get()  # Get age input
    weight = entryWeight.get()  # Get weight input
    height = entryHeight.get()  # Get height input

    try:
        weight = float(weight)  # Convert weight to float
        height = float(height)  # Convert height to float

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Construct BMI result message
        resultMessage = f"Name: {name}\nAge: {age}\nBMI: {bmi:.2f}\n"
        
        # Display BMI result
        messagebox.showinfo("BMI Result", resultMessage)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight and height.")  # Show error message box

# Create input fields and labels
labelName = tk.Label(mainWindow, text="Name:")
labelName.pack()
entryName = tk.Entry(mainWindow)
entryName.pack()

labelAge = tk.Label(mainWindow, text="Age:")
labelAge.pack()
entryAge = tk.Entry(mainWindow)
entryAge.pack()

labelWeight = tk.Label(mainWindow, text="Weight (kg):")
labelWeight.pack()
entryWeight = tk.Entry(mainWindow)
entryWeight.pack()

labelHeight = tk.Label(mainWindow, text="Height (m):")
labelHeight.pack()
entryHeight = tk.Entry(mainWindow)
entryHeight.pack()

# Create button to calculate BMI
calculateButton = tk.Button(mainWindow, text="Calculate BMI", command=calculateBmi)
calculateButton.pack(pady=20)

mainWindow.mainloop()  # Enter main event loop
