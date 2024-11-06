import tkinter as tk
from tkinter import messagebox
def book_ride():
    
    name = name_entry.get()
    phone = phone_entry.get()
    pickup = pickup_entry.get()
    destination = destination_entry.get()
    vehicle_type = vehicle_var.get()

    
    if not name or not phone or not pickup or not destination or not vehicle_type:
        messagebox.showwarning("Input Error", "Please fill in all fields!")
    else:
        
        messagebox.showinfo("Booking Confirmed", f"Booking Details:\n\nName: {name}\nPhone: {phone}\nPick-Up: {pickup}\nDestination: {destination}\nVehicle Type: {vehicle_type}")
       
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        pickup_entry.delete(0, tk.END)
        destination_entry.delete(0, tk.END)
        vehicle_var.set(None)
        
        root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("500x600")
# root.configure(bg="#f0f8ff")


title_label = tk.Label(root, text="Cab/Auto Booking", font=("Arial", 18, "bold"))
title_label.pack(pady=20)


name_label = tk.Label(root, text="Full Name:", font=("Arial", 12))
name_label.pack(anchor="w", padx=20)
name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5, padx=20)


phone_label = tk.Label(root, text="Phone Number:", font=("Arial", 12))
phone_label.pack(anchor="w", padx=20)
phone_entry = tk.Entry(root, font=("Arial", 12), width=30)
phone_entry.pack(pady=5, padx=20)

pickup_label = tk.Label(root, text="Pick-Up Location:", font=("Arial", 12))
pickup_label.pack(anchor="w", padx=20)
pickup_entry = tk.Entry(root, font=("Arial", 12), width=30)
pickup_entry.pack(pady=5, padx=20)

destination_label = tk.Label(root, text="Destination:", font=("Arial", 12))
destination_label.pack(anchor="w", padx=20)
destination_entry = tk.Entry(root, font=("Arial", 12), width=30)
destination_entry.pack(pady=5, padx=20)

vehicle_label = tk.Label(root, text="Select Vehicle Type:", font=("Arial", 12))
vehicle_label.pack(anchor="w", padx=20, pady=10)

vehicle_var = tk.StringVar()

car_rb = tk.Radiobutton(root, text="Car", variable=vehicle_var, value="Car", font=("Arial", 12))
auto_rb = tk.Radiobutton(root, text="Auto", variable=vehicle_var, value="Auto", font=("Arial", 12))

car_rb.pack(anchor="w", padx=20)
auto_rb.pack(anchor="w", padx=20)

submit_button = tk.Button(root, text="Book Ride", font=("Arial", 14), bg="#4CAF50", fg="white", command=book_ride)
submit_button.pack(pady=20)

root.mainloop()