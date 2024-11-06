import tkinter as tk
from tkinter import messagebox



def submit_transaction():
    sender_acc = sender_account_entry.get()
    receipent_acc = recipient_account_entry.get()
    amount = amount_entry.get()
    description = description_entry.get("1.0", tk.END).strip()
    if not sender_acc or not receipent_acc or not amount:
        messagebox.showwarning("Input Error ","Please fill in all required documnet")
        return 
    messagebox.showinfo("Transcation Successful","The transaction has been processed successfully")
    sender_account_entry.delete(0,tk.END)
    receipent_account_entry.delete(0,tk.END)
    amount_entry.delete(0,tk.END)
    description_entry.delete("1.0",tk.END)





def cancel_transaction():
    sender_account_entry.delete(0, tk.END)
    recipient_account_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete("1.0", tk.END)
    messagebox.showinfo("Transaction Canceled", "The transaction has been canceled.")



root = tk.Tk()
root.title("Fund Transfer")
root.geometry("400x400")
root.resizable(False, False)



tk.Label(root, text="Sender Account Number:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
sender_account_entry = tk.Entry(root, width=30)
sender_account_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="Recipient Account Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
recipient_account_entry = tk.Entry(root, width=30)
recipient_account_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Label(root, text="Amount:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
amount_entry = tk.Entry(root, width=30)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Description:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
description_entry = tk.Text(root, width=30, height=4)
description_entry.grid(row=3, column=1, padx=10, pady=10)


submit_button = tk.Button(root, text="Submit", command=submit_transaction, bg="green", fg="white")
submit_button.grid(row=4, column=0, padx=10, pady=20)

cancel_button = tk.Button(root, text="Cancel", command=cancel_transaction, bg="red", fg="white")
cancel_button.grid(row=4, column=1, padx=10, pady=20)


root.mainloop()


