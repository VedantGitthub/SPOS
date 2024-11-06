import tkinter as tk

# Function to close the Help window
def close_help():
    help_window.destroy()

# Initialize main window
help_window = tk.Tk()
help_window.title("Help Screen")
help_window.geometry("400x300")

# Help message label
help_label = tk.Label(help_window, text="Help Instructions", font=("Arial", 18, "bold"))
help_label.pack(pady=20)

# Detailed instructions
help_text = tk.Label(help_window, text="1. To register, fill in your details.\n"
                                       "2. To book a ride, enter pick-up location and destination.\n"
                                       "3. To navigate through the app, use the buttons at the bottom.",
                     font=("Arial", 12), justify="left")
help_text.pack(padx=20, pady=10)

# Close Button
close_button = tk.Button(help_window, text="Close", font=("Arial", 14), command=close_help)
close_button.pack(pady=20)

# Run the Help window
help_window.mainloop()
