import tkinter as tk
import ttkbootstrap as ttk
from convert import convert_to_kilometer


# window
window = ttk.Window(themename='superhero')
window.title("Converter")
window.geometry("800x600")

# tittle
title_label = ttk.Label(master=window, text="Miles to kilometers converter", font='Calibri 16 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(
    master=input_frame,
    text="Convert",
    command=lambda: convert_to_kilometer(entry_int, output_string))

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output field
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Kilometers: ',
    font='Calibri 16 bold',
    textvariable=output_string)
output_label.pack(pady=5)


# run the window
window.mainloop()
