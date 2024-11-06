import tkinter as tk
from tkinter import messagebox




def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    department = department_var.get()
    comments = comments_text.get("1.0", tk.END).strip()
    symptoms = []
    
    if fever_check.get():
        symptoms.append("Fever")
    if cough_check.get():
        symptoms.append("Cough")
    if fatigue_check.get():
        symptoms.append("Fatigue")
    if headache_check.get():
        symptoms.append("Headache")
    
    if not name:
        messagebox.showwarning("Incomplete Form", "Please enter the patient's name.")
    elif not age.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid age.")
    elif gender == "Select":
        messagebox.showwarning("Incomplete Form", "Please select a gender.")
    elif department == "Select Department":
        messagebox.showwarning("Incomplete Form", "Please select a department.")
    else:
        registration_info = f"Patient Name: {name}\nAge: {age}\nGender: {gender}\n"
        registration_info += f"Department: {department}\nSymptoms: {', '.join(symptoms) if symptoms else 'None'}\n"
        registration_info += f"Additional Comments: {comments if comments else 'No comments.'}\n"
        
        messagebox.showinfo("Form Submitted", f"Thank you for registering.\n\n{registration_info}")
        root.destroy()  




root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("500x550")
root.configure(bg="#e6f7ff")


title_label = tk.Label(root, text="Patient Registration Form", font=("Arial", 16, "bold"), bg="#e6f7ff", fg="#003366")
title_label.pack(pady=10)


name_frame = tk.Frame(root, bg="#e6f7ff")
name_frame.pack(pady=5, fill="x", padx=20)
tk.Label(name_frame, text="Name:", font=("Arial", 12), bg="#e6f7ff").pack(side="left")
name_entry = tk.Entry(name_frame, width=30, font=("Arial", 10))
name_entry.pack(side="left", padx=10)


age_frame = tk.Frame(root, bg="#e6f7ff")
age_frame.pack(pady=5, fill="x", padx=20)
tk.Label(age_frame, text="Age:", font=("Arial", 12), bg="#e6f7ff").pack(side="left")
age_entry = tk.Entry(age_frame, width=10, font=("Arial", 10))
age_entry.pack(side="left", padx=10)


gender_frame = tk.Frame(root, bg="#e6f7ff")
gender_frame.pack(pady=5, fill="x", padx=20)
tk.Label(gender_frame, text="Gender:", font=("Arial", 12), bg="#e6f7ff").pack(side="left")
gender_var = tk.StringVar(value="Select")
gender_menu = tk.OptionMenu(gender_frame, gender_var, "Male", "Female", "Other")
gender_menu.config(width=15, font=("Arial", 10))
gender_menu.pack(side="left", padx=10)


department_frame = tk.Frame(root, bg="#e6f7ff")
department_frame.pack(pady=5, fill="x", padx=20)
tk.Label(department_frame, text="Department:", font=("Arial", 12), bg="#e6f7ff").pack(side="left")
department_var = tk.StringVar(value="Select Department")
department_menu = tk.OptionMenu(department_frame, department_var, "General Medicine", "Pediatrics", "Cardiology", "Orthopedics", "Dermatology", "Gynecology")
department_menu.config(width=15, font=("Arial", 10))
department_menu.pack(side="left", padx=10)


symptoms_frame = tk.Frame(root, bg="#e6f7ff")
symptoms_frame.pack(pady=10, fill="x", padx=20)
tk.Label(symptoms_frame, text="Symptoms:", font=("Arial", 12), bg="#e6f7ff").pack(anchor="w")
fever_check = tk.BooleanVar()
cough_check = tk.BooleanVar()
fatigue_check = tk.BooleanVar()
headache_check = tk.BooleanVar()
tk.Checkbutton(symptoms_frame, text="Fever", variable=fever_check, font=("Arial", 10), bg="#e6f7ff").pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Cough", variable=cough_check, font=("Arial", 10), bg="#e6f7ff").pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Fatigue", variable=fatigue_check, font=("Arial", 10), bg="#e6f7ff").pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Headache", variable=headache_check, font=("Arial", 10), bg="#e6f7ff").pack(anchor="w")


comments_frame = tk.Frame(root, bg="#e6f7ff")
comments_frame.pack(pady=10, fill="x", padx=20)
tk.Label(comments_frame, text="Additional Comments:", font=("Arial", 12), bg="#e6f7ff").pack(anchor="w")
comments_text = tk.Text(comments_frame, width=40, height=4, font=("Arial", 10))
comments_text.pack(pady=5)


submit_button = tk.Button(root, text="Submit Registration", command=submit_form, font=("Arial", 12), bg="#4CAF50", fg="white", width=20)
submit_button.pack(pady=20)

# Run the main event loop
root.mainloop()

