import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Interactive Python Calculator")
root.geometry("400x500")  # Larger window
root.resizable(False, False)  # Fixed size

# Entry widget to display expressions
entry = tk.Entry(root, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10, padx=10, sticky="nsew")

# Function to handle button clicks
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('=', 5, 1, 3)
]

# Add buttons to the window
for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) > 3 else 1

    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    else:
        action = lambda x=text: button_click(x)

    tk.Button(
        root, text=text, width=8, height=3, font=('Arial', 18),
        command=action, bg="#1e1e1e", fg="white", relief="ridge"
    ).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Adjust grid row/column weights
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
