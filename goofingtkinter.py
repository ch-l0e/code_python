import tkinter as tk

root = tk.Tk()
root.title("Frogs are cool")
root.geometry("300x200")
label = tk.Label(root, text = "frogs are cool because they are cool.", font = ("Times New Roman", 10))
label.pack()

def closeapp():
    root.destroy()

button = tk.Button(root, text = "exit", command = closeapp)
button.pack()

root.mainloop()