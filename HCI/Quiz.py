import tkinter as tk
from tkinter import messagebox



questions = [
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "Which is the national bird of India?",
    "What is the square root of 64?",
]
options = [
    ["Mumbai", "Kolkalte", "New Delhi", "Bangalore"],
    ["Earth", "Mars", "Jupiter", "Saturn"],
    ["Peacock", "Crow", "Sparrow", "Parrot"],
    ["6", "7", "8", "9"],
]
answers = ["New Delhi", "Mars", "Peacock", "8"]


current_question = 0
score = 0



def submit_answer():
    global score, current_question
    
    selected_option = option_var.get()
    if selected_option == answers[current_question]:
        score += 1
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect", f"The correct answer was: {answers[current_question]}")
    
    
    next_button.config(state=tk.NORMAL)



def next_question():
    global current_question

    current_question += 1
    if current_question >= len(questions):
        messagebox.showinfo("Quiz Completed", f"Your score is {score}/{len(questions)}")
        root.destroy()  
    else:
        
        question_label.config(text=questions[current_question])
        for i in range(4):
            option_buttons[i].config(text=options[current_question][i])
        
        
        option_var.set(None)
        next_button.config(state=tk.DISABLED)




root = tk.Tk()
root.title("Online Quiz")
root.geometry("500x400")
root.configure(bg="#f0f5f9")


title_label = tk.Label(root, text="Online Quiz", font=("Arial", 18, "bold"), bg="#f0f5f9", fg="#333")
title_label.pack(pady=10)


question_label = tk.Label(root, text=questions[current_question], font=("Arial", 14), bg="#f0f5f9", wraplength=400, justify="center")
question_label.pack(pady=20)


option_var = tk.StringVar(value=None)


option_buttons = []
for i in range(4):
    btn = tk.Checkbutton(root, text=options[current_question][i], variable=option_var, onvalue=options[current_question][i], offvalue="", font=("Arial", 12), bg="#f0f5f9", anchor="w")
    btn.pack(fill="x", padx=50, pady=5)
    option_buttons.append(btn)


submit_button = tk.Button(root, text="Submit", command=submit_answer, font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
submit_button.pack(pady=10)


next_button = tk.Button(root, text="Next", command=next_question, font=("Arial", 12), bg="#2196F3", fg="white", width=10, state=tk.DISABLED)
next_button.pack(pady=10)


root.mainloop()

