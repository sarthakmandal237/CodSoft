import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        equation = entry.get()
        result = eval(equation)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input or operation")


root = tk.Tk()
root.title("Calculator")
root.configure(bg="#303030")


entry = tk.Entry(root, width=20, font=('Arial', 20,'bold'))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


button_config = {'padx': 15, 'pady': 15, 'width': 2, 'height': 1, 'font': ('Arial', 12)}


buttons = ['7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', 'C', '=', '+']

r = 1
c = 0
for btn_text in buttons:
    if btn_text == '=':
        equals_button = tk.Button(root, text=btn_text, command=calculate, **button_config,bg="#757575",fg="white")
        equals_button.grid(row=r, column=c, padx=5, pady=5)
    elif btn_text == 'C':
        clear_button = tk.Button(root, text=btn_text, command=lambda: entry.delete(0, tk.END), **button_config,bg="#424242",fg="white")
        clear_button.grid(row=r, column=c, padx=5, pady=5)
    else:
        btn = tk.Button(root, text=btn_text, command=lambda t=btn_text: entry.insert(tk.END, t), **button_config,bg="#424242",fg="white")
        btn.grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()
