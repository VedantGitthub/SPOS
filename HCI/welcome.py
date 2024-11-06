import tkinter as tk

# Function to handle the 'Start' button click
def start_app():
    welcome_label.config(text="Welcome to the App!")
    start_button.config(state="disabled")  # Disable button after click

# Initialize main window
root = tk.Tk()
root.title("Welcome Screen")
root.geometry("400x200")

# Welcome message label
welcome_label = tk.Label(root, text="Welcome to the Application", font=("Arial", 18, "bold"))
welcome_label.pack(pady=40)

# Start button
start_button = tk.Button(root, text="Start", font=("Arial", 14), command=start_app)
start_button.pack(pady=20)

# Run the application
root.mainloop()
