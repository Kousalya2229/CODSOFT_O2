import tkinter as tk
from tkinter import messagebox

history = []

def calculate(event=None):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected")
            return

        result_text = f"{num1} {operation} {num2} = {result}"
        result_label.config(text="Result: " + str(result))
        history.append(result_text)
        update_history()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
    entry1.focus()

def update_history():
    history_listbox.delete(0, tk.END)
    for item in history[-5:]:  
        history_listbox.insert(tk.END, item)


root = tk.Tk()
root.title("Smart Calculator")
root.geometry("320x400")
root.resizable(False, False)


tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()


tk.Label(root, text="Choose operation:").pack(pady=5)
operator = tk.StringVar(root)
operator.set('+')
tk.OptionMenu(root, operator, '+', '-', '*', '/').pack()


tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
tk.Button(root, text="Clear", command=clear).pack()


result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)


tk.Label(root, text="History (Last 5):").pack()
history_listbox = tk.Listbox(root, height=5)
history_listbox.pack(pady=5, fill=tk.BOTH, padx=20)


root.bind('<Return>', calculate)

entry1.focus()
root.mainloop()
