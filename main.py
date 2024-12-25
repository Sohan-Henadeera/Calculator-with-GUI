import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Calculation Function
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
        else:
            messagebox.showerror("Error", "Please select a valid operation!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

#Clear Function
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
    operation_var.set("Select Operation")

#WindowMain
root = tk.Tk()
root.title("Python Calculator")
root.geometry("550x500")
root.configure(bg="#48494a")

#Theme and Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TLabel", font=("Helvetica", 12), background="#48494a")
style.configure("TEntry", font=("Helvetica", 12))

#Fields
ttk.Label(root, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2 = ttk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

#Dropdowns
operation_var = tk.StringVar(value="Select Operation")
operations_menu = ttk.OptionMenu(root, operation_var, "Select Operation", "Add", "Subtract", "Multiply", "Divide")
operations_menu.grid(row=2, column=0, columnspan=2, pady=10)

#Buttons
ttk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, pady=10, padx=10)
ttk.Button(root, text="Clear", command=clear).grid(row=3, column=1, pady=10, padx=10)

#Results
result_label = ttk.Label(root, text="Result: ", font=("Helvetica", 14, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()