import tkinter as tk
from tkinter import ttk

def convert_temp():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_var.set(f"{celsius:.2f} °C")
    except ValueError:
        celsius_var.set("Invalid input")

# Main window
root = tk.Tk()
root.title("TempCalculator")
root.geometry("600x350")
root.resizable(True, True)
root.configure(bg="#8A2BE2")  # Purple background

# Header Label (38px)
header = tk.Label(root, text="Fahrenheit to Celsius", font=("Arial", 38),
                  bg="#8A2BE2", fg="white")
header.pack(pady=(20, 10))

# Input Frame
frame = tk.Frame(root, bg="#8A2BE2")
frame.pack(pady=10)

# Fahrenheit Entry (252x44, 16px text, corner-radius simulated)
fahrenheit_entry = ttk.Entry(frame, font=("Arial", 16), width=20)
fahrenheit_entry.insert(0, "Fahrenheit...")
fahrenheit_entry.grid(row=0, column=0, padx=22, pady=10, ipady=10)

# Calculate Button (115x44, 16px text)
calc_button = ttk.Button(frame, text="Calculate", command=convert_temp)
calc_button.grid(row=0, column=1, padx=22, pady=10, ipadx=10, ipady=5)

# Celsius Output Label (161x44, 16px text, corner-radius simulated)
celsius_var = tk.StringVar()
celsius_label = tk.Label(root, textvariable=celsius_var, font=("Arial", 16),
                         width=20, height=2, bg="white", fg="black",
                         relief="solid", bd=1)
celsius_label.pack(pady=20)

root.mainloop()