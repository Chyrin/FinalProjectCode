# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk

import messagebox
from PIL import ImageTk, Image

# Create the main window
main_window = tk.Tk()
main_window.geometry("800x800")
main_window.title("Car Dealership Application")

# Create the car selection window
car_selection_window = tk.Toplevel(main_window)
car_selection_window.geometry("400x400")
car_selection_window.title("Car Selection")
car_selection_window.withdraw()

#Car Data
CAR_BRANDS = {
    "Toyota": [
        {"name": "Corolla", "price": 20000},
        {"name": "Camry", "price": 25000},
        {"name": "Rav4", "price": 30000},
    ],
    "Honda": [
        {"name": "Civic", "price": 22000},
        {"name": "Accord", "price": 27000},
        {"name": "CR-V", "price": 30000},
    ],
    "Ford": [
        {"name": "Focus", "price": 18000},
        {"name": "Fusion", "price": 23000},
        {"name": "Escape", "price": 28000},
    ],
    "Chevrolet": [
        {"name": "Cruze", "price": 20000},
        {"name": "Malibu", "price": 25000},
        {"name": "Equinox", "price": 30000},
    ],
    "Nissan": [
        {"name": "Sentra", "price": 22000},
        {"name": "Altima", "price": 27000},
        {"name": "Rogue", "price": 30000},
    ],
}

#Data For Selected Price Button
def show_selected_price(image_label=None):
    selected_brand = brand_var.get()
    selected_car = car_var.get()
    price = [car["price"] for car in CAR_BRANDS[selected_brand] if car["name"] == selected_car][0]
    messagebox.showinfo("Car Price", f"Selected Car: {selected_car}\nPrice: ${price}")

#Home Page Logo(Dealership Logo)
pic_frame = tk.Frame(main_window, width=450, height=350)
pic_frame.place(anchor="center", relx=0.5, rely=0.5)
imga = ImageTk.PhotoImage(Image.open("logo.jpg"))
image_label = tk.Label(pic_frame, image=imga)
image_label.pack(pady=10)


def update_car_options(*args):
    selected_brand = brand_var.get()
    car_options = [car["name"] for car in CAR_BRANDS[selected_brand]]
    car_var.set(car_options[0])
    car_menu["menu"].delete(0, "end")
    for car in car_options:
        car_menu["menu"].add_command(label=car, command=tk._setit(car_var, car))


def open_car_selection_window():
    selected_brand = brand_var.get()
    selected_car = car_var.get()

    if not selected_brand or not selected_car:
        messagebox.showerror("Error", "Please select a car brand and a car before opening the car selection window.")
        return
    main_window.withdraw()
    car_selection_window.update()
    car_selection_window.deiconify()

def open_main_window():
    car_selection_window.withdraw()
    main_window.update()
    main_window.deiconify()

def exit_application():
    if messagebox.askokcancel("Exit Application", "Do you want to exit the application?"):
        main_window.quit()

#Second Image
pic_twoframe = tk.Frame(car_selection_window, width=200, height=200)
pic_twoframe.place(anchor="center", relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("r34.jpg"))
image_label = tk.Label(pic_twoframe, image=img)
image_label.pack(pady=10)

# Create a label for the car brands
brand_label = tk.Label(main_window, text="Select a Car Brand:")
brand_label.pack(pady=10)

# Create a variable to store the selected car brand
brand_var = tk.StringVar()

# Create a dropdown menu for car brands
brand_menu = tk.OptionMenu(main_window, brand_var, *CAR_BRANDS.keys())
brand_menu.pack()

# Create a label for the car options
car_label = tk.Label(main_window, text="Select a Car:")
car_label.pack(pady=10)

# Create a variable to store the selected car
car_var = tk.StringVar()

# Create a dropdown menu for car options
car_menu = tk.OptionMenu(main_window, car_var, "")
car_menu.pack()

# Bind the update_car_options function to the brand_var so that the car options update when the brand is changed
brand_var.trace("w", update_car_options)

# Create a button to show the selected car's price
price_button = tk.Button(car_selection_window, text="Show Price", command=show_selected_price)
price_button.pack(pady=10)

# Create a button to open the car selection window
open_button = tk.Button(main_window, text="Open Car Selection", command=open_car_selection_window)
open_button.pack(pady=10)

# Create a variable to store the selected car
selected_car_var = tk.StringVar()

# Create radio buttons for car selection
car_radios = []
for brand, cars in CAR_BRANDS.items():
    if brand == brand_var.get():
        for car in cars:
            car_radios.append(tk.Radiobutton(car_selection_window, text=car["name"], variable=selected_car_var, value=car["name"]))
            car_radios[-1].pack()

# Create a button to go back to the main window
back_button = tk.Button(car_selection_window, text="Back", command=open_main_window)
back_button.pack(pady=10)

# Create an exit button
exit_button = tk.Button(main_window, text="Exit", command=exit_application)
exit_button.pack(pady=10)

main_window.mainloop()
