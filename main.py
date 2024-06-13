import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Remy GUI")
window.geometry("800x600")

# tittle
title_label = ttk.Label(master=window, text="Miles to kilometers converter", font='Calibri 16 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Convert")
entry.pack(side='left')
button.pack(side='left')
input_frame.pack()

# run the window
window.mainloop()