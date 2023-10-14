import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    complexity = complexity_var.get()
    
    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length Label and Entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Complexity Label and Radio Buttons
complexity_label = tk.Label(root, text="Complexity:")
complexity_label.pack()
complexity_var = tk.StringVar()
complexity_var.set("Low")
low_button = tk.Radiobutton(root, text="Low", variable=complexity_var, value="Low")
medium_button = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium")
high_button = tk.Radiobutton(root, text="High", variable=complexity_var, value="High")
low_button.pack()
medium_button.pack()
high_button.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Result Label
result_label = tk.Label(root, text="", wraplength=200)
result_label.pack()

# Run the GUI
root.mainloop()
