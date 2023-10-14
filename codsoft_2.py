import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current_text = screen.get()
        current_text += text
        screen.set(current_text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 40 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
]

row, col = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="lucida 25", width=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
    button.bind("<Button-1>", on_button_click)

root.mainloop()
