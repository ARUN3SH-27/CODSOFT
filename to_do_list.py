import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

def add_task():
    task_text = task_entry.get()
    if task_text:
        tasks_listbox.insert("end", task_text)
        task_entry.delete(0, "end")

        # Set the font size for the newly added task
        tasks_listbox.itemconfig("end", font=("Courier New", 25))

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def mark_as_complete():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task_text = tasks_listbox.get(task_index)
        if not task_text.startswith("~~"):
            tasks_listbox.delete(task_index)
            tasks_listbox.insert(task_index, "~~" + task_text)
        else:
            tasks_listbox.delete(task_index)
            tasks_listbox.insert(task_index, task_text[2:])  # Remove the strikethrough prefix

def change_color():
    new_color = askcolor()[1]
    if new_color:
        update_colors(new_color)

def update_colors(new_color):
    root.configure(bg=new_color)
    # Set text color based on background color
    text_color = "white" if new_color == "#000000" else "black"  # Use hex code for black
    style.configure("Custom.TButton", background=new_color, foreground=text_color)
    tasks_listbox.config(bg=new_color, fg=text_color)
    task_entry.config(fg="black", insertbackground="black")  # Set text entry color and cursor color

root = tk.Tk()
root.title("To-Do List")

style = ttk.Style()
style.configure("Custom.TButton", background="green", foreground="white")

tasks_frame = ttk.Frame(root)
tasks_frame.pack(fill="both", expand=True)

# Use a monospaced font to maintain alignment
monospace_font = ("Courier New", 15)

tasks_listbox = tk.Listbox(tasks_frame, bg="lightgray", fg="black", font=monospace_font, selectmode="single")
tasks_listbox.pack(fill="both", expand=True)

task_entry = tk.Entry(root, fg="black", insertbackground="black", font=monospace_font)
task_entry.pack(pady=5)

add_task_button = tk.Button(root, text="Add Task", command=add_task, foreground="black")
add_task_button.pack()

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, foreground="black")
delete_task_button.pack()

mark_complete_button = tk.Button(root, text="Mark as Complete", command=mark_as_complete, foreground="black")
mark_complete_button.pack()

color_button = tk.Button(root, text="Change Color", command=change_color, foreground="black")
color_button.pack()

root.configure(bg="lightblue")

root.mainloop()
