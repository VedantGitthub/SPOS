import tkinter as tk
from tkinter import messagebox
def submit_feedback():
    name = name_entry.get()
    food_quality = food_quality_var.get()
    service_quality = service_quality_var.get()
    comments = comments_text.get("1.0", tk.END).strip()
    feedback_points = []
    
    if quality_check_var.get():
        feedback_points.append("Food Quality")
    if service_check_var.get():
        feedback_points.append("Service")
    if ambiance_check_var.get():
        feedback_points.append("Ambiance")
    
    if not name:
        messagebox.showwarning("Incomplete Form", "Please enter your name.")
    elif food_quality == "Select" or service_quality == "Select":
        messagebox.showwarning("Incomplete Form", "Please rate both food quality and service quality.")
    else:
        feedback_text = f"Thank you for your feedback, {name}!\n\n"
        feedback_text += f"Food Quality: {food_quality}\nService Quality: {service_quality}\n"
        feedback_text += f"Checked Feedback Points: {', '.join(feedback_points) if feedback_points else 'None'}\n"
        feedback_text += f"Additional Comments: {comments if comments else 'No comments.'}\n"
        
        messagebox.showinfo("Feedback Submitted", feedback_text)
        root.destroy()  
        
root = tk.Tk()
root.title("Customer Feedback Form")
root.geometry("450x500")
root.configure(bg="#f0f5f9")


title_label = tk.Label(root, text="Customer Feedback Form", font=("Arial", 16, "bold"), bg="#f0f5f9", fg="#333")
title_label.pack(pady=10)


name_frame = tk.Frame(root, bg="#f0f5f9")
name_frame.pack(pady=5, fill="x", padx=20)
tk.Label(name_frame, text="Name:", font=("Arial", 12), bg="#f0f5f9").pack(side="left")
name_entry = tk.Entry(name_frame, width=30, font=("Arial", 10))
name_entry.pack(side="left", padx=10)


food_quality_frame = tk.Frame(root, bg="#f0f5f9")
food_quality_frame.pack(pady=5, fill="x", padx=20)
tk.Label(food_quality_frame, text="Food Quality:", font=("Arial", 12), bg="#f0f5f9").pack(side="left")
food_quality_var = tk.StringVar(value="Select")
food_quality_options = ["Excellent", "Good", "Average", "Poor"]
food_quality_menu = tk.OptionMenu(food_quality_frame, food_quality_var, *food_quality_options)
food_quality_menu.config(width=15, font=("Arial", 10))
food_quality_menu.pack(side="left", padx=10)


service_quality_frame = tk.Frame(root, bg="#f0f5f9")
service_quality_frame.pack(pady=5, fill="x", padx=20)
tk.Label(service_quality_frame, text="Service Quality:", font=("Arial", 12), bg="#f0f5f9").pack(side="left")
service_quality_var = tk.StringVar(value="Select")
service_quality_options = ["Excellent", "Good", "Average", "Poor"]
service_quality_menu = tk.OptionMenu(service_quality_frame, service_quality_var, *service_quality_options)
service_quality_menu.config(width=15, font=("Arial", 10))
service_quality_menu.pack(side="left", padx=10)


checkbox_frame = tk.Frame(root, bg="#f0f5f9")
checkbox_frame.pack(pady=10, fill="x", padx=20)
quality_check_var = tk.BooleanVar()
service_check_var = tk.BooleanVar()
ambiance_check_var = tk.BooleanVar()
tk.Checkbutton(checkbox_frame, text="Food Quality", variable=quality_check_var, font=("Arial", 10), bg="#f0f5f9").pack(side="left", padx=5)
tk.Checkbutton(checkbox_frame, text="Service", variable=service_check_var, font=("Arial", 10), bg="#f0f5f9").pack(side="left", padx=5)
tk.Checkbutton(checkbox_frame, text="Ambiance", variable=ambiance_check_var, font=("Arial", 10), bg="#f0f5f9").pack(side="left", padx=5)


comments_frame = tk.Frame(root, bg="#f0f5f9")
comments_frame.pack(pady=10, fill="x", padx=20)
tk.Label(comments_frame, text="Additional Comments:", font=("Arial", 12), bg="#f0f5f9").pack(anchor="w")
comments_text = tk.Text(comments_frame, width=40, height=4, font=("Arial", 10))
comments_text.pack(pady=5)


submit_button = tk.Button(root, text="Submit Feedback", command=submit_feedback, font=("Arial", 12), bg="#4CAF50", fg="white", width=20)
submit_button.pack(pady=20)


root.mainloop()