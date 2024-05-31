import tkinter as tk

window = tk.Tk()

window.geometry("500x300")
window.title("Shape Creator")

label = tk.Label(window, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(window, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Create Shape", font=('Arial', 18))
button.pack(padx=10, pady=10)

window.mainloop()