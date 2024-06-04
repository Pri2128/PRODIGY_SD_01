import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    temperature = float(temperature_entry.get())
    unit = original_unit_combobox.get().lower()
    result_text.delete('1.0', tk.END)

    if unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        result_text.insert(tk.END, f"{temperature} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
    elif unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        result_text.insert(tk.END, f"{temperature} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
    elif unit == 'kelvin':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        result_text.insert(tk.END, f"{temperature} Kelvin is equal to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")
    else:
        result_text.insert(tk.END, "Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")

# Create main window
root = tk.Tk()
root.title("Temperature Conversion")

# Create input frame
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Temperature entry
ttk.Label(input_frame, text="Temperature:").grid(row=0, column=0, sticky=tk.W)
temperature_entry = ttk.Entry(input_frame, width=10)
temperature_entry.grid(row=0, column=1, padx=5, pady=5)

# Unit selection combobox
ttk.Label(input_frame, text="Original Unit:").grid(row=1, column=0, sticky=tk.W)
original_unit_combobox = ttk.Combobox(input_frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=10)
original_unit_combobox.grid(row=1, column=1, padx=5, pady=5)
original_unit_combobox.set("Celsius")

# Convert button
convert_button = ttk.Button(input_frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result text
result_text = tk.Text(root, wrap=tk.WORD, height=5, width=50)
result_text.grid(row=1, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
