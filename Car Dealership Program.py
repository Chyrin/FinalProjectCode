#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

# Dictionary of car brands and their corresponding cars with names and prices
CAR_BRANDS = {
    "Toyota": [
        {"name": "Corolla", "price": 20000},
        {"name": "Camry", "price": 25000},
        {"name": "Rav4", "price": 30000},
        {"name": "Highlander", "price": 35000},
        {"name": "Prius", "price": 28000},
    ],
    "Honda": [
        {"name": "Civic", "price": 22000},
        {"name": "Accord", "price": 27000},
        {"name": "CR-V", "price": 30000},
        {"name": "Pilot", "price": 36000},
        {"name": "Insight", "price": 25000},
    ],
    "Ford": [
        {"name": "Focus", "price": 18000},
        {"name": "Fusion", "price": 23000},
        {"name": "Escape", "price": 28000},
        {"name": "Explorer", "price": 32000},
        {"name": "Mustang", "price": 40000},
    ],
    "Chevrolet": [
        {"name": "Cruze", "price": 19000},
        {"name": "Malibu", "price": 24000},
        {"name": "Equinox", "price": 29000},
        {"name": "Traverse", "price": 33000},
        {"name": "Camaro", "price": 45000},
    ],
    "Nissan": [
        {"name": "Sentra", "price": 21000},
        {"name": "Altima", "price": 26000},
        {"name": "Rogue", "price": 31000},
        {"name": "Pathfinder", "price": 35000},
        {"name": "370Z", "price": 42000},
    ],
    # Add more car brands and their cars with names and prices here
}

def show_selected_price():
    selected_brand = brand_var.get()
    selected_car = car_var.get()
    price = [car["price"] for car in CAR_BRANDS[selected_brand] if car["name"] == selected_car][0]
    messagebox.showinfo("Car Price", f"Selected Car: {selected_car}\nPrice: ${price}")

def update_car_options(*args):
    selected_brand = brand_var.get()
    car_options = [car["name"] for car in CAR_BRANDS[selected_brand]]
    car_var.set(car_options[0])
    car_menu["menu"].delete(0, "end")
    for car in car_options:
        car_menu["menu"].add_command(label=car, command=tk._setit(car_var, car))

# Create the main window
window = tk.Tk()
window.title("Car Dealership Application")

# Create a label for the car brands
brand_label = tk.Label(window, text="Select a Car Brand:")
brand_label.pack(pady=10)

# Create a variable to store the selected car brand
brand_var = tk.StringVar()

# Create a dropdown menu for car brands
brand_menu = tk.OptionMenu(window, brand_var, *CAR_BRANDS.keys())
brand_menu.pack()

# Create a label for the car options
car_label = tk.Label(window, text="Select a Car:")
car_label.pack(pady=10)

# Create a variable to store the selected car
car_var = tk.StringVar()

# Create a dropdown menu for car options
car_menu = tk.OptionMenu(window, car_var, "")
car_menu.pack()

# Bind the update_car_options function to the brand_var so that the car options update when the brand is changed
brand_var.trace("w", update_car_options)

# Create a button to show the selected car's price
price_button = tk.Button(window, text="Show Price", command=show_selected_price)
price_button.pack(pady=10)

# Start the main event loop
window.mainloop()


# In[ ]:




